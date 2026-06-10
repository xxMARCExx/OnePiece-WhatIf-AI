import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import save

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY")
)

VOICE_ID = "BNgbHR0DNeZixGQVzloa"


def text_to_speech(text, output_file="output/voice.mp3"):
    audio = client.text_to_speech.convert(
        voice_id=VOICE_ID,
        model_id="eleven_multilingual_v2",
        text=text
    )

    save(audio, output_file)

    return output_file