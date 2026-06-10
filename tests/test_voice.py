from context_builder import build_context
from claude_client import call_claude
from voice_generator import run_voice_pipeline

# Step 1: generate script (same as your system)
idea = "What if Luffy never met Zoro?"

script = call_claude(build_context(idea))

print("\n================ SCRIPT ================\n")
print(script)

# Step 2: convert script → voice narration text
voice_text = run_voice_pipeline(script)

print("\n================ VOICE SCRIPT ================\n")
print(voice_text)