import whisper

whisper_model = whisper.load_model("small")

def transcribe_speech(file_with_speech):
    res = whisper_model.transcribe(file_with_speech, language="ru")
    print(res["text"])

    return res