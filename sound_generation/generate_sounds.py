# Importing libraries
from scipy.io.wavfile import write
import numpy as np
import colorednoise as cn

# Generate a Brownian noise audio file
def generate_noise(filename, sample_rate, duration):
    
    # Noise generation
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False) 
    noise_signal = cn.powerlaw_psd_gaussian(2, sample_rate * duration)  # 2: brown noise, 0: white noise

    factor = 40 
    left_signal = noise_signal * factor
    right_signal = noise_signal * factor

    stereo_signal = np.column_stack((left_signal, right_signal))

    # Normalization
    max_value = np.max(np.abs(stereo_signal))
    if max_value > 1.0:
        stereo_signal /= max_value

    # Saving
    write(filename, sample_rate, (stereo_signal * 32767).astype(np.int16))

# Calculate the amplitude of the square wave used for the isochronic tones
def generate_amplitude(duration, amp_0, amp_1):
    t = np.linspace(0, duration, int(duration * 44100), endpoint=False)

    square_wave = np.zeros_like(t)

    # Defining a period
    square_period = amp_0 + amp_1
    square_time = t % square_period
    square_wave[square_time < amp_0] = 0
    square_wave[(square_time >= amp_0) & (square_time < square_period)] = 1
    return square_wave

# Generate a Brownian noise and isochronic tones audio file
def generate_isochronic_tones_noise(filename, sample_rate, duration, freq, amp_0, amp_1):
    dt = 1 / sample_rate
    number_times = int(duration / dt)
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Generate isochronic tones
    amplitude = generate_amplitude(duration, amp_0, amp_1)
    signal = np.sin(2 * np.pi * freq * t)
    isochronic_signal = np.multiply(amplitude, signal)

    # Generate Brownian noise
    noise_signal = cn.powerlaw_psd_gaussian(2, sample_rate * duration)  # 2: brown noise, 0: white noise

    # Combine isochronic tones and noise
    tone_factor = 0.05 
    noise_factor = 40 

    left_signal = (isochronic_signal * tone_factor + noise_signal * noise_factor)
    right_signal = (isochronic_signal * tone_factor + noise_signal * noise_factor)
    stereo_signal = np.column_stack((left_signal, right_signal))

    # Normalization
    max_value = np.max(np.abs(stereo_signal))
    if max_value > 1.0:
        stereo_signal /= max_value

    # Saving
    write(filename, sample_rate, (stereo_signal * 32767).astype(np.int16))


# Parameters
duration = 540  # in seconds
frequency = 500  # in Hz
amp_0 = 0.05  # pause duration
amp_1 = 0.05  # sound duration

# Generate audio files
generate_isochronic_tones_noise('./isochronic_tones_noise.wav', 44100, duration, frequency, amp_0, amp_1)
generate_noise('./noise.wav', 44100, duration)
