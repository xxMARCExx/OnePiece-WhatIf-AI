import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pipeline.voice_generator import run_voice_pipeline
from context_builder import build_context
from claude_client import call_claude
from pipeline.tts_generator import text_to_speech

idea = "What if Luffy never met Zoro?"

# Step 1: script
script = call_claude(build_context(idea))
print("\nSCRIPT:\n", script)

# Step 2: clean voice text
voice_text = run_voice_pipeline(script)
print("\nVOICE TEXT:\n", voice_text)

# Step 3: generate audio
audio_file = text_to_speech(voice_text)

print("\nAUDIO GENERATED:", audio_file)