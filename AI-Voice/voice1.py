import torch
import torchaudio
import torch.nn as nn
import torch.nn.functional as F

import IPython

from tortoise.api import TextToSpeech
from tortoise.utils.audio import load_audio, load_voice, load_voices


text = "Thanks for reading this article. I hope you learned something."

# Pick a "preset mode" to determine quality. Options: {"ultra_fast", "fast" (default), "standard", "high_quality"}. See docs in api.py
preset = "fast"


CUSTOM_VOICE_NAME = "ejemplo1"

import os
from google.colab import files

custom_voice_folder = f"tortoise/voices/{CUSTOM_VOICE_NAME}"
os.makedirs(custom_voice_folder)
for i, file_data in enumerate(files.upload().values()):
  with open(os.path.join(custom_voice_folder, f'{i}.wav'), 'wb') as f:
    f.write(file_data)


# Generate speech with the custotm voice.
voice_samples, conditioning_latents = load_voice(CUSTOM_VOICE_NAME)
gen = tts.tts_with_preset(text, voice_samples=voice_samples, conditioning_latents=conditioning_latents, 
                          preset=preset)
torchaudio.save(f'generated-{CUSTOM_VOICE_NAME}.wav', gen.squeeze(0).cpu(), 24000)
IPython.display.Audio(f'generated-{CUSTOM_VOICE_NAME}.wav')
#Descargar audio en tu equipo:
from google.colab import files; files.download(f'generated-{CUSTOM_VOICE_NAME}.wav')