"""
r6_story_scene.py — RECONSTRUCTED Blender pipeline for the "offline-rendered" videos (V2, V3, V6;
plausibly V1/V5). NOT original source. TESTED headless with bpy 4.2 (Cycles CPU), see
16_VALIDATION_REPORT.md.

Reproduces three signatures that are hard/impossible in a live Roblox capture but trivial here:
  1. per-limb MOTION BLUR (V3 f2119–2123 arms blurred while torso is sharp; V6 run cycle)
  2. SHADOW WITHOUT ITS OWNER (V1: a shadow on the wall that does not match the visible pose)
     -> object.visible_camera = False, still casts shadows
  3. SELECTIVE REFLECTION (V6 81–85 s: only Lily is reflected in the frozen pond, the brother is not)
     -> object.visible_glossy = False on the brother
Plus: R6 rig from primitives with joint pivots, instant face swaps via keyframed (CONSTANT
interpolation) mix factor, eased camera push-in, 576x1024 @ 30 fps output.

Run:  python r6_story_scene.py --out /tmp/r6 [--frames 1-60] [--engine CYCLES|BLENDER_EEVEE_NEXT]
      (or: blender -b -P r6_story_scene.py -- --out /tmp/r6)
"""
import argparse, math, os, sys
import bpy

FPS = 30
S = 0.4  # stud scale (same convention as the Three.js reconstruction)


# ----------------------------------------------------------------------------- helpers
def mat(name, color, rough=0.7, emission=None):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*color, 1); b.inputs["Roughness"].default_value = rough
    if emission:
        b.inputs["Emission Color"].default_value = (*emission, 1); b.inputs["Emission Strength"].default_value = 3
    return m


def cube(name, size, loc, material, parent=None):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
    o = bpy.context.active_object; o.name = name
    o.scale = size; bpy.ops.object.transform_apply(scale=True)
    o.data.materials.append(material)
    if parent: o.parent = parent
    o.location = loc
    return o


def empty(name, loc, parent=None):
    o = bpy.data.objects.new(name, None); bpy.context.collection.objects.link(o)
    if parent: o.parent = parent
    o.location = loc
    return o


def face_material(name, skin, expressions):
    """Face = procedural 'eyes + mouth' per expression mixed by an integer-stepped factor.
    In production you'd use one Image Texture per decal; procedural keeps the script self-contained."""
    m = bpy.data.materials.new(name); m.use_nodes = True
    nt = m.node_tree; nodes, links = nt.nodes, nt.links
    bsdf = nodes["Principled BSDF"]; bsdf.inputs["Roughness"].default_value = 0.8
    # value node driven by keyframes: 0 = neutral, 1 = shock
    sel = nodes.new("ShaderNodeValue"); sel.name = "expr"; sel.outputs[0].default_value = 0
    tc = nodes.new("ShaderNodeTexCoord")
    sep = nodes.new("ShaderNodeSeparateXYZ"); links.new(tc.outputs["Generated"], sep.inputs[0])
    # eyes: two dots whose radius grows with 'expr' (round shocked eyes); mouth: a bar that becomes an 'o'
    def dot(cx, cy, r_expr0, r_expr1):
        dx = nodes.new("ShaderNodeMath"); dx.operation = 'SUBTRACT'; dx.inputs[1].default_value = cx; links.new(sep.outputs[0], dx.inputs[0])
        dy = nodes.new("ShaderNodeMath"); dy.operation = 'SUBTRACT'; dy.inputs[1].default_value = cy; links.new(sep.outputs[2], dy.inputs[0])
        l = nodes.new("ShaderNodeCombineXYZ"); links.new(dx.outputs[0], l.inputs[0]); links.new(dy.outputs[0], l.inputs[1])
        ln = nodes.new("ShaderNodeVectorMath"); ln.operation = 'LENGTH'; links.new(l.outputs[0], ln.inputs[0])
        r = nodes.new("ShaderNodeMapRange"); r.inputs[3].default_value = r_expr0; r.inputs[4].default_value = r_expr1
        links.new(sel.outputs[0], r.inputs[0])
        lt = nodes.new("ShaderNodeMath"); lt.operation = 'LESS_THAN'; links.new(ln.outputs[1], lt.inputs[0]); links.new(r.outputs[0], lt.inputs[1])
        return lt
    e1, e2 = dot(0.35, 0.62, 0.05, 0.09), dot(0.65, 0.62, 0.05, 0.09)
    mouth = dot(0.5, 0.3, 0.07, 0.06)
    add = nodes.new("ShaderNodeMath"); add.operation = 'MAXIMUM'; links.new(e1.outputs[0], add.inputs[0]); links.new(e2.outputs[0], add.inputs[1])
    add2 = nodes.new("ShaderNodeMath"); add2.operation = 'MAXIMUM'; links.new(add.outputs[0], add2.inputs[0]); links.new(mouth.outputs[0], add2.inputs[1])
    mix = nodes.new("ShaderNodeMix"); mix.data_type = 'RGBA'
    mix.inputs[6].default_value = (*skin, 1); mix.inputs[7].default_value = (0.02, 0.02, 0.02, 1)
    links.new(add2.outputs[0], mix.inputs[0]); links.new(mix.outputs[2], bsdf.inputs["Base Color"])
    return m


def build_r6(name, origin, shirt, pants, skin=(1.0, 0.78, 0.2), hair=(0.12, 0.07, 0.04)):
    root = empty(f"{name}_root", origin)
    hips = empty(f"{name}_hips", (0, 0, 2 * S), root)
    cube(f"{name}_torso", (2 * S, 1 * S, 2 * S), (0, 0, 1 * S), mat(f"{name}_shirt", shirt), hips)
    neck = empty(f"{name}_neck", (0, 0, 2 * S), hips)
    fm = face_material(f"{name}_face", skin, ["neutral", "shock"])
    head = cube(f"{name}_head", (1.2 * S, 1.2 * S, 1.2 * S), (0, 0, 0.6 * S), fm, neck)
    cube(f"{name}_hair", (1.3 * S, 1.3 * S, 0.45 * S), (0, 0.03 * S, 0.5 * S), mat(f"{name}_hairm", hair, 0.5), head)
    joints = {"root": root, "hips": hips, "neck": neck, "head": head}
    for side, x in (("L", -1.5), ("R", 1.5)):
        sh = empty(f"{name}_{side}shoulder", (x * S, 0, 1.9 * S), hips)
        cube(f"{name}_{side}arm", (1 * S, 1 * S, 2 * S), (0, 0, -0.9 * S), mat(f"{name}_{side}armm", shirt), sh)
        joints[f"{side}shoulder"] = sh
        hp = empty(f"{name}_{side}hip", (x / 3 * S, 0, 0), hips)
        cube(f"{name}_{side}leg", (1 * S, 1 * S, 2 * S), (0, 0, -1 * S), mat(f"{name}_{side}legm", pants), hp)
        joints[f"{side}hip"] = hp
    return joints


def key_rot(obj, frame, x=0.0, interp='BEZIER'):
    obj.rotation_euler = (x, 0, 0); obj.keyframe_insert("rotation_euler", frame=frame)
    for fc in obj.animation_data.action.fcurves:
        for kp in fc.keyframe_points:
            if kp.co[0] == frame: kp.interpolation = interp


def walk_cycle(j, f0, f1, cycle_frames=16, amp=0.6, dist_per_cycle=1.1, start_y=0.0):
    """Pendulum R6 walk: legs/arms in opposition, root advances by stride per cycle (no foot skate)."""
    for f in range(f0, f1 + 1, cycle_frames // 4):
        ph = (f - f0) / cycle_frames * 2 * math.pi
        s = math.sin(ph)
        key_rot(j["Lhip"], f, s * amp); key_rot(j["Rhip"], f, -s * amp)
        key_rot(j["Lshoulder"], f, -s * amp); key_rot(j["Rshoulder"], f, s * amp)
        j["hips"].location.z = 2 * S + abs(math.cos(ph)) * 0.025; j["hips"].keyframe_insert("location", frame=f)
    j["root"].location.y = start_y; j["root"].keyframe_insert("location", frame=f0)
    j["root"].location.y = start_y - (f1 - f0) / cycle_frames * dist_per_cycle; j["root"].keyframe_insert("location", frame=f1)
    for fc in j["root"].animation_data.action.fcurves: [setattr(k, "interpolation", 'LINEAR') for k in fc.keyframe_points]


def alarm_gesture(j, f0):
    """V3 'screamed': anticipation (2 f) -> raise with overshoot (5 f) -> settle (6 f)."""
    for side in ("L", "R"):
        sh = j[f"{side}shoulder"]
        key_rot(sh, f0, 0.0); key_rot(sh, f0 + 2, 0.15); key_rot(sh, f0 + 7, -2.35); key_rot(sh, f0 + 13, -2.05)


def set_face(head_obj, frame, value):
    node = head_obj.active_material.node_tree.nodes["expr"]
    node.outputs[0].default_value = value
    node.outputs[0].keyframe_insert("default_value", frame=frame)
    fcs = head_obj.active_material.node_tree.animation_data.action.fcurves
    for fc in fcs:
        for kp in fc.keyframe_points: kp.interpolation = 'CONSTANT'   # instant decal-style swap


# ----------------------------------------------------------------------------- scene
def build(engine="CYCLES"):
    bpy.ops.wm.read_factory_settings(use_empty=True)
    sc = bpy.context.scene
    sc.render.resolution_x, sc.render.resolution_y, sc.render.fps = 576, 1024, FPS
    sc.frame_start, sc.frame_end = 1, 60
    sc.render.engine = engine
    if engine == "CYCLES":
        sc.cycles.samples = 24; sc.cycles.use_denoising = True; sc.cycles.device = 'CPU'
    sc.render.use_motion_blur = True; sc.render.motion_blur_shutter = 0.5   # 180° shutter
    sc.view_settings.view_transform = 'AgX'; sc.view_settings.look = 'AgX - Medium High Contrast'

    world = bpy.data.worlds.new("sky"); sc.world = world; world.use_nodes = True
    world.node_tree.nodes["Background"].inputs[0].default_value = (0.95, 0.55, 0.35, 1)   # sunset sky (V6)
    world.node_tree.nodes["Background"].inputs[1].default_value = 0.6

    # frozen pond: glossy, slightly rough, dark -> blurred reflection like V6
    bpy.ops.mesh.primitive_plane_add(size=40, location=(0, 0, 0))
    ice = bpy.context.active_object; ice.data.materials.append(mat("ice", (0.25, 0.2, 0.3), rough=0.08))
    # wall for the shadow trick (V1)
    wall = cube("wall", (8, 0.3, 4), (0, 2.5, 2), mat("wall", (0.92, 0.9, 0.86), 0.9))

    sun = bpy.data.lights.new("sun", 'SUN'); sun.energy = 4; sun.angle = math.radians(3)   # angle -> soft penumbra
    sun.color = (1.0, 0.75, 0.55)
    so = bpy.data.objects.new("sun", sun); bpy.context.collection.objects.link(so)
    so.rotation_euler = (math.radians(55), 0, math.radians(20))   # sun behind camera, pointing +Y onto the wall

    hero = build_r6("hero", (-0.9, 0, 0), shirt=(0.85, 0.25, 0.08), pants=(0.1, 0.12, 0.25))
    lily = build_r6("lily", (0.9, 0, 0), shirt=(0.85, 0.2, 0.4), pants=(0.15, 0.1, 0.2))
    ghost = build_r6("shadowcaster", (0.0, 1.2, 0), shirt=(1, 1, 1), pants=(1, 1, 1))

    # 2. shadow without owner: invisible to camera AND reflections, still casts shadows on the wall
    for o in bpy.data.objects:
        if o.name.startswith("shadowcaster") and o.type == 'MESH':
            o.visible_camera = False; o.visible_glossy = False
    alarm_gesture(ghost, 1)               # the shadow "acts" a different pose than anyone visible

    # 3. selective reflection: the brother is not reflected by the ice
    for o in bpy.data.objects:
        if o.name.startswith("hero_") and o.type == 'MESH':
            o.visible_glossy = False

    # 1. motion: hero walks, then the alarm gesture (motion blur shows on the fast arm raise)
    walk_cycle(hero, 1, 32, start_y=1.5)
    alarm_gesture(hero, 34)
    set_face(hero["head"], 1, 0.0); set_face(hero["head"], 34, 1.0)     # instant swap on the gesture

    # camera: slow push-in, Bezier ease in/out (the corpus' dominant move)
    cam = bpy.data.cameras.new("cam"); cam.lens = 35; cam.sensor_fit = 'VERTICAL'
    co = bpy.data.objects.new("cam", cam); bpy.context.collection.objects.link(co); sc.camera = co
    target = empty("cam_target", (0, 0, 1.4))
    tc = co.constraints.new('TRACK_TO'); tc.target = target; tc.track_axis = 'TRACK_NEGATIVE_Z'; tc.up_axis = 'UP_Y'
    co.location = (0.4, -9.0, 1.6); co.keyframe_insert("location", frame=1)
    co.location = (0.3, -6.5, 1.55); co.keyframe_insert("location", frame=60)
    for fc in co.animation_data.action.fcurves:
        for kp in fc.keyframe_points:
            kp.interpolation = 'SINE'; kp.easing = 'EASE_IN_OUT'
    return sc


if __name__ == "__main__":
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else sys.argv[1:]
    ap = argparse.ArgumentParser(); ap.add_argument("--out", default="/tmp/r6"); ap.add_argument("--frames", default="1,20,36,40")
    ap.add_argument("--engine", default="CYCLES"); a = ap.parse_args(argv)
    sc = build(a.engine); os.makedirs(a.out, exist_ok=True)
    for f in [int(x) for x in a.frames.split(",")]:
        sc.frame_set(f); sc.render.filepath = os.path.join(a.out, f"f{f:04d}.png")
        bpy.ops.render.render(write_still=True)
        print("rendered", sc.render.filepath)
