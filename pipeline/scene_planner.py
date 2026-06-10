from claude_client import call_claude

def build_scene_plan(script):
    prompt = f"""
You are a strict TikTok video editor.

Convert this script into EXACTLY 5 scenes.

RULES:
- Do NOT exceed 2 sentences per scene
- Do NOT add extra commentary
- Every scene must be complete
- No scene can be longer than 3 lines total
- Do NOT stop early

SCRIPT:
{script}

OUTPUT:

SCENE 1:
TIME:
VISUAL:
NARRATION:
EMOTION:

(repeat for all 5 scenes)
...
"""
    return call_claude(prompt)