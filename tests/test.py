from scene_planner import build_scene_plan
from context_builder import build_context
from claude_client import call_claude

script = call_claude(build_context("What if Luffy never met Zoro?"))

print(build_scene_plan(script))