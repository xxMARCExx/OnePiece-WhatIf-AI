from claude_client import call_claude
import re
from pipeline.script_compressor import compress_script


def generate_voice_script(script):
    prompt = f"""
You are writing a "What If One Piece" narration.

OUTPUT ONLY SPOKEN NARRATION.

STYLE:
- dark butterfly effect storytelling
- philosophical tone allowed
- single timeline cause → effect

STRICT RULES:
- MUST start with "What if"
- Maximum 6 sentences
- Must be under 35 seconds spoken
- No montage storytelling
- No multiple arcs
- No extra characters
- No explanations

SCRIPT:
{script}
"""
    return call_claude(prompt)


def clean_voice_text(text):
    text = re.sub(r"(HOOK|DIVERGENCE|CHAIN OF EVENTS|WORLD IMPACT|TWIST ENDING).*?:", "", text)
    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"\n+", " ", text)
    return text.strip()


def run_voice_pipeline(script):
    compressed_script = compress_script(script)
    voice_text = generate_voice_script(compressed_script)
    voice_text = clean_voice_text(voice_text)

    with open("output/voice_script.txt", "w", encoding="utf-8") as f:
        f.write(voice_text)

    return voice_text