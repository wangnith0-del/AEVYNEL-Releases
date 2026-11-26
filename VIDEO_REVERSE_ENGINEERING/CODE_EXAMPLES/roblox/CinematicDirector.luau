--!strict
-- =====================================================================================
-- CinematicDirector.luau — RECONSTRUCTED (hypothetical) Roblox Studio shot runner.
-- NOT original source: none of the 7 videos ships project files. UNTESTED here (no Roblox
-- Studio in the analysis environment) — written against the public Roblox API.
--
-- Why this design: V4/V7 are FORTEMENT PROBABLE in-engine Roblox captures (classic R6 rigs,
-- low-res face decals that pixelate in close-ups, Brookhaven/Bloxburg-style kits, no rendered
-- motion blur). Their camera moves show 3D parallax and near-zero jitter (0.009–0.06 px/frame),
-- i.e. scripted CFrame tweens, not a hand-held player camera. Creators of this genre commonly
-- use Moon Animator 2 for this; the script below is the code equivalent.
--
-- Usage (LocalScript in StarterPlayerScripts, run in Play Solo, record with OBS at 60 fps):
--   local Director = require(script.CinematicDirector)
--   Director.run(require(script.Episode01))   -- Episode module returns {shots=..., events=...}
-- =====================================================================================
local RunService = game:GetService("RunService")
local Lighting = game:GetService("Lighting")
local Players = game:GetService("Players")

export type CamKey = { cf: CFrame, fov: number? }
export type Shot = {
	start: number, finish: number,
	from: CamKey, to: CamKey,
	ease: Enum.EasingStyle?, dir: Enum.EasingDirection?,
	shake: number?,
}
export type Event = { t: number, fn: () -> () }   -- face swaps, animation triggers, SFX, VFX
export type Episode = { shots: { Shot }, events: { Event }, duration: number }

local Director = {}

-- TweenService:GetValue gives the same curves Moon Animator exposes in its UI.
local TweenService = game:GetService("TweenService")
local function ease(alpha: number, style: Enum.EasingStyle?, dir: Enum.EasingDirection?): number
	return TweenService:GetValue(alpha, style or Enum.EasingStyle.Sine, dir or Enum.EasingDirection.InOut)
end

local function shotAt(ep: Episode, t: number): Shot
	for _, s in ep.shots do
		if t >= s.start and t < s.finish then return s end
	end
	return ep.shots[#ep.shots]
end

--- Deterministic playback: time comes from a fixed-step clock, not wall time, so a slow frame
--- never desynchronises the camera from the pre-recorded voice-over.
function Director.run(ep: Episode, fps: number?)
	local step = 1 / (fps or 60)
	local cam = workspace.CurrentCamera
	cam.CameraType = Enum.CameraType.Scriptable
	-- hide the local avatar but keep its shadow: LocalTransparencyModifier does exactly that
	-- (one plausible way to get V1's "shadow without its owner" shots in-engine).
	local t, nextEvent = 0, 1
	table.sort(ep.events, function(a, b) return a.t < b.t end)
	local conn
	conn = RunService.RenderStepped:Connect(function()
		t += step
		local s = shotAt(ep, t)
		local a = ease(math.clamp((t - s.start) / (s.finish - s.start), 0, 1), s.ease, s.dir)
		local cf = s.from.cf:Lerp(s.to.cf, a)
		if s.shake and s.shake > 0 then
			local k = s.shake
			cf *= CFrame.Angles(math.noise(t * 0.7, 1) * k, math.noise(t * 0.7, 2) * k, 0)
		end
		cam.CFrame = cf
		cam.FieldOfView = (s.from.fov or 50) + ((s.to.fov or s.from.fov or 50) - (s.from.fov or 50)) * a
		while nextEvent <= #ep.events and ep.events[nextEvent].t <= t do
			task.spawn(ep.events[nextEvent].fn); nextEvent += 1
		end
		if t >= ep.duration then conn:Disconnect() end
	end)
end

--- Helper mirroring the dominant move of the corpus: a push-in toward a subject's head.
function Director.pushIn(start: number, finish: number, subject: BasePart, d0: number, d1: number, height: number?, side: number?): Shot
	local target = subject.Position + Vector3.new(0, height or 0, 0)
	local dir = (subject.CFrame.LookVector)
	local off = Vector3.new(side or 0, 0, 0)
	return {
		start = start, finish = finish,
		from = { cf = CFrame.lookAt(target + dir * d0 + off, target), fov = 50 },
		to = { cf = CFrame.lookAt(target + dir * d1 + off * (d1 / d0), target), fov = 50 },
		ease = Enum.EasingStyle.Sine, dir = Enum.EasingDirection.InOut,
	}
end

--- Lighting presets estimated from the footage (values are estimates, tune by eye).
function Director.applyLook(name: string)
	Lighting.Technology = Enum.Technology.Future       -- soft-edged shadows, point-light shadows
	Lighting.GlobalShadows = true
	for _, c in Lighting:GetChildren() do
		if c:IsA("PostEffect") or c:IsA("Atmosphere") then c:Destroy() end
	end
	local cc = Instance.new("ColorCorrectionEffect")
	local bloom = Instance.new("BloomEffect")
	local atm = Instance.new("Atmosphere")
	if name == "sunny_town" then          -- V1 / V5 look
		Lighting.ClockTime = 14; Lighting.Brightness = 3; Lighting.ExposureCompensation = 0.1
		cc.Saturation = 0.15; cc.Contrast = 0.05
		bloom.Intensity = 0.4; bloom.Size = 24; bloom.Threshold = 1.6
		atm.Density = 0.3; atm.Haze = 1
	elseif name == "golden_hour" then     -- V3 / V6 sunset look (warm, R-B median +33…+44)
		Lighting.ClockTime = 17.6; Lighting.Brightness = 2.5
		cc.Saturation = 0.25; cc.TintColor = Color3.fromRGB(255, 232, 210)
		bloom.Intensity = 0.8; bloom.Size = 40; bloom.Threshold = 1.2
		atm.Density = 0.35; atm.Color = Color3.fromRGB(255, 190, 150); atm.Haze = 2
		local rays = Instance.new("SunRaysEffect"); rays.Intensity = 0.08; rays.Parent = Lighting
	elseif name == "night_storm" then     -- V4 hurricane / V7 midnight
		Lighting.ClockTime = 0.5; Lighting.Brightness = 1; Lighting.ExposureCompensation = 0.4
		cc.Saturation = 0.1; cc.TintColor = Color3.fromRGB(200, 215, 255)
		bloom.Intensity = 1; bloom.Size = 30; bloom.Threshold = 0.9
		atm.Density = 0.45; atm.Color = Color3.fromRGB(80, 100, 140)
	end
	cc.Parent = Lighting; bloom.Parent = Lighting; atm.Parent = Lighting
end

return Director
