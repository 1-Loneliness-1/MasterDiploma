import logging
import time
from typing import Dict
from PyQt6.QtCore import QObject, pyqtSignal

from audio_recorder import AudioRecorder
from audio_transcriber import AudioTranscriber
from ner import MedicalNER


class AudioProcessor(QObject):
    entities_recognition_done = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.recorder = None
        self.transcriber = None
        self.nlp = None
        self.recording_active = False

    def start_process(self):
        if not self.recording_active:
            self.recording_active = True
            self._start_recording()

    def stop_process(self):
        self.recording_active = False

    def _start_recording(self):
        logging.debug("Запуск записи...")
        self.rec_start = time.perf_counter()
        self.recorder = AudioRecorder(duration=5)  # 5 секунд записи
        self.recorder.signal_with_result.connect(self.handle_audio_ready)
        self.recorder.signal_with_error.connect(self.handle_error)
        self.recorder.start()

    def handle_audio_ready(self, file_path):
        self.rec_end = time.perf_counter()
        self.recorder = None

        self.transcriber = AudioTranscriber(file_path)
        self.transcriber.signal_with_result.connect(self.handle_transcription)
        self.transcriber.signal_with_error.connect(self.handle_error)
        self.transcript_start = time.perf_counter()
        self.transcriber.start()

    def handle_transcription(self, text):
        self.transcript_end = time.perf_counter()
        self.transcriber = None

        self.nlp = MedicalNER(text)
        self.nlp.signal_with_res.connect(self.handle_ner_done)
        self.nlp.signal_with_error.connect(self.handle_error)
        self.nlp_start = time.perf_counter()
        self.nlp.start()

    def handle_ner_done(self, entities_dictionary: Dict):
        self.nlp_end = time.perf_counter()
        print(f"Запись: {self.rec_end - self.rec_start:.2f} c.")
        print(f"Транскрибирование: {self.transcript_end - self.transcript_start:.2f} c.")
        print(f"Распознавание сущностей: {self.nlp_end - self.nlp_start:.2f} c.")
        self.nlp = None
        self.entities_recognition_done.emit(entities_dictionary)

        # Повторяем цикл, если активен
        if self.recording_active:
            self._start_recording()

    def handle_error(self, error):
        logging.error(f"Ошибка: {error}")
        self.transcriber = None
        self.recorder = None
        self.nlp = None
        # При ошибке остановим цикл
        self.recording_active = False
