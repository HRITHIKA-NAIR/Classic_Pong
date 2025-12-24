import numpy as np
import wave
import struct

def generate_sound(filename, freq, duration=0.2, volume=0.5, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration))
    wave_data = volume * np.sin(2 * np.pi * freq * t)

    with wave.open(filename, 'w') as wav_file:
        n_channels = 1
        sampwidth = 2
        n_frames = len(wave_data)
        comptype = 'NONE'
        compname = 'not compressed'
        wav_file.setparams((n_channels, sampwidth, sample_rate, n_frames, comptype, compname))

        for sample in wave_data:
            wav_file.writeframes(struct.pack('h', int(sample * 32767)))

# Create sounds
generate_sound("paddle_hit.wav", freq=400)   # lower pop
generate_sound("score.wav", freq=700)        # higher ding
