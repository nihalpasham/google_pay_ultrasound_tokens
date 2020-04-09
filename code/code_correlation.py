
from code_signal import code_construct
from load_wavfile import load_wavfile
import numpy as np
import matplotlib.pyplot as plt

path_to_file = 'some_wav_file'
upsampled_signal = code_construct()
re, im, number_of_complex_samples, _ = load_wavfile(path_to_file)


def code_correlate(upsampled_signal, re, im):
    
    number_of_code_samples = len(upsampled_signal)
    # so that we dont overshoot when sliding the code signal forward
    range_ = (int(number_of_complex_samples/number_of_code_samples)-1)*number_of_code_samples

    correlation_magnitude_buffer = []
    normalized_correlation_magnitude_buffer = []

    for i in range(0, int(range_)):
        real_correl = np.correlate(upsampled_signal, re[ i  : i + len(upsampled_signal) ])[0]
        imag_correl = np.correlate(upsampled_signal, im[ i  : i + len(upsampled_signal) ])[0]

        correlation_magnitude = real_correl + imag_correl      
        normalized_correl_magnitude = correlation_magnitude**2
        
        correlation_magnitude_buffer.append(correlation_magnitude)
        normalized_correlation_magnitude_buffer.append(normalized_correl_magnitude)
        

    print(len(correlation_magnitude_buffer))
    print(max(correlation_magnitude_buffer))
    print(len(normalized_correlation_magnitude_buffer))
    print(max(normalized_correlation_magnitude_buffer))

    plt.figure(figsize=(20,10))
    plt.plot((normalized_correlation_magnitude_buffer[10:10000]))
    plt.xlabel('time in (ms)')
    plt.ylabel('correlation')
    plt.title('Code-Signal cross correlation')
    plt.show()

    return normalized_correlation_magnitude_buffer