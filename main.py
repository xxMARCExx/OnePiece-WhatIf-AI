from pipeline.voice_generator import run_voice_pipeline
from pipeline.tts_generator import text_to_speech


def run_full_pipeline(idea):
    print("\n🎬 Generating script...")

    voice_text = run_voice_pipeline(idea)

    print("\n🧠 Voice Text:\n", voice_text)

    print("\n🎤 Converting to speech...")

    audio_file = text_to_speech(voice_text)

    print("\n✅ DONE:", audio_file)

    return audio_file


if __name__ == "__main__":
    idea = "What if Luffy never met Zoro?"
    run_full_pipeline(idea)