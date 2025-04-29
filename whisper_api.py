import torch.cuda
import whisper
from PyQt6.QtCore import QThread, pyqtSignal

class Transcriber(QThread):

    signal_with_res = pyqtSignal(str)
    signal_with_error = pyqtSignal(str)

    def __init__(self, file_with_speech):
        super().__init__()

        self.file_for_transcribe = file_with_speech

    def run(self):
        try:
            device = 'cuda' if torch.cuda.is_available() else 'cpu'
            whisper_model = whisper.load_model("small").to(device)
            res = whisper_model.transcribe(self.file_for_transcribe, language="ru")
            print(res["text"])
            self.signal_with_res.emit(res["text"])
        except Exception as e:
            self.signal_with_error.emit(f"Error: {e}")