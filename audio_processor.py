import logging

from PyQt6.QtCore import QObject, pyqtSignal
from audio_recorder import AudioRecorder
from audio_transcriber import AudioTranscriber

class AudioProcessor(QObject):
    transcription_done = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.recorder = None
        self.transcriber = None

    def start_process(self):
        self.recorder = AudioRecorder()
        self.recorder.signal_with_result.connect(self.handle_audio_ready)
        self.recorder.start()

    def handle_audio_ready(self, file_path):
        logging.debug(f"Получен аудиофайл: {file_path}")
        self.recorder = None  # Освобождаем recorder

        self.transcriber = AudioTranscriber(file_path)
        self.transcriber.signal_with_result.connect(self.handle_transcription)
        self.transcriber.signal_with_error.connect(self.handle_error)
        self.transcriber.start()

    def handle_transcription(self, text):
        logging.debug("Транскрипция завершена")
        self.transcription_done.emit(text)
        self.transcriber = None

    def handle_error(self, error):
        logging.error(f"Ошибка: {error}")