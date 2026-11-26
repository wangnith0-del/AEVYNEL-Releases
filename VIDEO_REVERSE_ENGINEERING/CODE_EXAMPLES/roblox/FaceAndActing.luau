--!strict
-- =====================================================================================
-- FaceAndActing.luau — RECONSTRUCTED (hypothetical) expression + acting helpers. UNTESTED.
--
-- Observed: faces are 2D decals swapped instantaneously (V7 f4812→f4814: neutral line mouth →
-- open triangle mouth with no in-between). "Talking" is not phoneme lip-sync: the mouth decal
-- is swapped on stressed words / shouts (V4 'Wake up!' alternates two decals). Tears, sweat
-- drops and blush are part of the decal art.
-- =====================================================================================
local TweenService = game:GetService("TweenService")

local Acting = {}

-- Map expression names to decal asset ids (fill with your own uploaded face textures).
Acting.Faces = {
	neutral = "rbxassetid://0", smile = "rbxassetid://0", shock = "rbxassetid://0",
	sad = "rbxassetid://0", yell = "rbxassetid://0", sleep = "rbxassetid://0",
}

function Acting.setFace(character: Model, expr: string)
	local head = character:FindFirstChild("Head") :: BasePart?
	if not head then return end
	local face = head:FindFirstChild("face") :: Decal?
	if face then face.Texture = Acting.Faces[expr] or Acting.Faces.neutral end
end

--- Blink by swapping to the 'sleep' face for 4 frames @30 fps (~0.13 s), every 2.5–4.5 s.
function Acting.autoBlink(character: Model, getExpr: () -> string)
	task.spawn(function()
		while character.Parent do
			task.wait(2.5 + math.random() * 2)
			local e = getExpr()
			if e == "neutral" or e == "smile" then
				Acting.setFace(character, "sleep"); task.wait(0.13); Acting.setFace(character, getExpr())
			end
		end
	end)
end

--- "Talk" = alternate open/closed mouth decals on a word list's timestamps (from Whisper JSON).
function Acting.talk(character: Model, words: { { s: number, e: number } }, t0: number, openFace: string, closedFace: string)
	for _, w in words do
		task.delay(w.s - t0, function() Acting.setFace(character, openFace) end)
		task.delay(w.e - t0, function() Acting.setFace(character, closedFace) end)
	end
end

--- Play a keyframed animation (exported from Moon Animator / Animation Editor) on a rig.
function Acting.play(character: Model, animId: string, fade: number?, speed: number?): AnimationTrack?
	local hum = character:FindFirstChildOfClass("Humanoid")
	local animator = hum and hum:FindFirstChildOfClass("Animator")
	if not animator then return nil end
	local a = Instance.new("Animation"); a.AnimationId = animId
	local track = (animator :: Animator):LoadAnimation(a)
	track:Play(fade or 0.15, 1, speed or 1)   -- 0.15 s cross-fade hides pose pops between clips
	return track
end

--- Walk a character to a point at a given speed, with the default walk cycle (Humanoid drives it).
function Acting.walkTo(character: Model, goal: Vector3, speed: number?)
	local hum = character:FindFirstChildOfClass("Humanoid")
	if not hum then return end
	hum.WalkSpeed = speed or 8            -- 8 studs/s reads as a calm walk on camera (default 16 = jog)
	hum:MoveTo(goal)
end

return Acting
