"""This module performs text to speech convertion"""

from dotenv import load_dotenv

import os
from io import BytesIO

from gtts import gTTS

from translate import Translator


load_dotenv()


def text_to_speech(context):
    """Function translates en to hi and generate audio data"""
    try:
        translator = Translator(to_lang="hi")
        translation = translator.translate(context)

        tts = gTTS(text=translation, lang='hi')

        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)

        audio_buffer.seek(0)

        return audio_buffer.read()

    except:
        print("Error during tts")
        return None
