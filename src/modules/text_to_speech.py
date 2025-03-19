"""This module performs text to speech convertion"""

from dotenv import load_dotenv

import os

from elevenlabs.client import ElevenLabs
from elevenlabs import save

from translate import Translator


load_dotenv()


def text_to_speech(context):
    """Function translates en to hi and generate audio data"""
    translator = Translator(to_lang="hi")
    translation = translator.translate(context)

    client = ElevenLabs(
        api_key=os.getenv("ELEVENLABS_API_KEY"),
    )

    audio = client.text_to_speech.convert(
        text=translation,
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128",
    )

    audio_data = b"".join(audio)

    return audio_data
