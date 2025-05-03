import os.path
import torch
import whisper
from ffmpeg_downloader.qt.wizard import QThread, pyqtSignal

class AudioTranscriber(QThread):

    signal_with_result = pyqtSignal(str)
    signal_with_error = pyqtSignal(str)

    def __init__(self, file_path_with_audio):
        super().__init__()

        self.file_path_with_audio = file_path_with_audio
        self.whisper_model = None

    def run(self):
        try:
            torch.cuda.empty_cache()
            if not os.path.exists(self.file_path_with_audio):
                raise FileNotFoundError(f"Файл {self.file_path_with_audio} не найден!")

            if self.whisper_model is None:
                device = "cuda" if torch.cuda.is_available() else "cpu"
                self.whisper_model = whisper.load_model("small", device = device)
            res = self.whisper_model.transcribe(
                self.file_path_with_audio,
                language="ru",
                fp16= False,
                no_speech_threshold=0.4
            )
            self.signal_with_result.emit(res["text"])
        except Exception as e:
            self.signal_with_error.emit(f"Ошибка: {e}")
        finally:
            if hasattr(self, 'filename') and os.path.exists(self.file_path_with_audio):
                os.remove(self.file_path_with_audio)