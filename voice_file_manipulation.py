import sounddevice
import soundfile
from pydub import AudioSegment


def audio_rec(output_file="speech.wav", duration=5, sample_rate=16000):
    speech_data = sounddevice.rec(
        int(duration * sample_rate),
        samplerate= sample_rate,
        channels= 1,
        dtype= 'int16'
    )
    sounddevice.wait()

    soundfile.write(output_file, speech_data, sample_rate)

    return audio_prep(output_file)

def audio_prep(input_file):
    current_audio = AudioSegment.from_file(input_file).normalize().strip_silence(silence_len=600, silence_thresh=-40)

    out_file = f"prep.wav"
    current_audio.export(out_file, format="wav")

    return out_file
