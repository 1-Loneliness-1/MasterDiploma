import openai
import whisper
from secret_api_key import WHISPER_API_KEY

openai.api_key = WHISPER_API_KEY

model = whisper.load_model("medium")
result = model.transcribe(audio="audio.wav", language="ru", model=model)
