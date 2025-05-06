import logging
from typing import Dict

from PyQt6.QtCore import QObject, pyqtSignal
from audio_recorder import AudioRecorder
from audio_transcriber import AudioTranscriber
from ner import MedicalWhisperNER


class AudioProcessor(QObject):
    entities_recognition_done = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.recorder = None
        self.transcriber = None
        self.nlp = None

    def start_process(self):
        self.recorder = AudioRecorder()
        self.recorder.signal_with_result.connect(self.handle_audio_ready)
        self.recorder.start()

    def handle_audio_ready(self, file_path):
        logging.debug(f"Получен аудиофайл: {file_path}")
        self.recorder = None

        self.transcriber = AudioTranscriber(file_path)
        self.transcriber.signal_with_result.connect(self.handle_transcription)
        self.transcriber.signal_with_error.connect(self.handle_error)
        self.transcriber.start()

    def handle_transcription(self, text):
        logging.debug("Транскрипция завершена")
        self.transcriber = None

        self.nlp = MedicalWhisperNER(text)
        self.nlp.signal_with_res.connect(self.handle_ner_done)
        self.nlp.start()

    def handle_ner_done(self, entities_dictionary: Dict):
        self.nlp = None
        self.entities_recognition_done.emit(entities_dictionary)

    def handle_error(self, error):
        self.transcriber = None
        self.recorder = None
        self.nlp = None
        logging.error(f"Ошибка: {error}")
