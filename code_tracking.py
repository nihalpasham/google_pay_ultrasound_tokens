
from code_correlation import code_correlate
from code_signal import code_construct
from load_wavfile import load_wavfile
import numpy as np

file_path = 'path_to_file'
re, im, number_of_complex_samples, data_shape = load_wavfile(file_path)
upsampled_signal = code_construct()

first_peak_index = 'You need find the first largest peak through visual inspection'  # Refer to jupyter notebook for more info


def code_tracking(first_peak_index, upsampled_signal, re, im):
    
    peaks = []
    normalized_correlation_magnitude_buffer = code_correlate(upsampled_signal, re, im)

    while True:
        
        v = max(normalized_correlation_magnitude_buffer[first_peak_index-200 : first_peak_index+200])

        s, = np.where(np.isclose(normalized_correlation_magnitude_buffer, v, rtol = 1e-09)) 
        # print('Index : {0}, Corr : {1}'.format(s, v))
        
        peaks.append([s[0],v])
        
        i = s[0] + 2032
                
        if i > data_shape-2032*2:
            print('done')
            return peaks
