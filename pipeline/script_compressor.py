from claude_client import call_claude

def compress_script(script):
    prompt = f"""
You are a TikTok story compressor.

Convert this into EXACTLY 5 events.

RULES:
- 5 events only
- Each event is ONE short sentence
- Max 8 words per event
- No emotion words
- No explanations
- No montage storytelling
- One timeline only (cause → effect)

FORMAT:
Event 1:
Event 2:
Event 3:
Event 4:
Event 5:

SCRIPT:
{script}
"""
    return call_claude(prompt)