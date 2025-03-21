"""This module performs text to speech convertion"""

import os
from io import BytesIO
import asyncio
import uuid

import aiofiles

from gtts import gTTS

from translate import Translator



async def text_to_speech(context):
    """Function translates en to hi and generate audio data"""
    try:
        translator = Translator(to_lang="hi")
        translation = translator.translate(context)

        tts = gTTS(text=translation, lang='hi')

        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)

        audio_buffer.seek(0)

        return audio_buffer.read()

    except Exception as e:
        print(f"Error during tts {e}")
        return None


async def text_to_speech_file(context):
    """
    Function creates a audio file from the text_to_speech
    and stored in a location with unique id and returns a path to the audio file
    """
    try:
        buffer_data = await text_to_speech(context)
        file_location = f"audio/{uuid.uuid4()}.mp3"
        os.makedirs('audio', exist_ok=True)
        async with aiofiles.open(file_location, "wb") as f:
            await f.write(buffer_data)

        return file_location
    except Exception as e:
        print(f"Error while creating file {e}")
        return None
