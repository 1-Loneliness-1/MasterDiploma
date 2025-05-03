import os
import wave
import pyaudio
from PyQt6.QtCore import QThread, pyqtSignal

class AudioRecorder(QThread):

    signal_with_result = pyqtSignal(str)
    signal_with_error = pyqtSignal(str)

    def __init__(self, sample_rate = 16000, duration = 5):
        super().__init__()
        self.sample_rate = sample_rate
        self.duration = duration

    def run(self):
        try:
            p = pyaudio.PyAudio()
            audio_stream = p.open(format=pyaudio.paInt16, channels=1, rate=self.sample_rate,
                                  input=True, frames_per_buffer=1024)
            frames = []
            for _ in range(0, int(self.sample_rate / 1024 * self.duration)):
                frames.append(audio_stream.read(1024))
            audio_stream.stop_stream()
            audio_stream.close()
            p.terminate()

            file_with_audio = "new_speech.wav"
            with wave.open(file_with_audio, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
                wf.setframerate(self.sample_rate)
                wf.writeframes(b''.join(frames))

            self.signal_with_result.emit(file_with_audio)
        except Exception as e:
            self.signal_with_error.emit(f"Ошибка записи! - {str(e)}")
