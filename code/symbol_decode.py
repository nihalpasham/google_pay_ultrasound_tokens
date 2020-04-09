
import numpy as np
from code_signal import code_construct
from code_tracking import code_tracking
from load_wavfile import load_wavfile
from scipy import signal
from scipy.signal import butter,filtfilt



first_peak_index = 'You need find the first largest peak through visual inspection'  # Refer to jupyter notebook for more info
path_to_file = 'some_input_wav_file'

upsampled_signal = code_construct()
re, im, number_of_complex_samples, _ = load_wavfile(path_to_file)
peaks = code_tracking(first_peak_index)

def symbol_decode(peaks, upsampled_signal, re, im):
    
    symbols_real = []
    symbols_imag = []

    base_freq = 100                     # This is in Hertz
    symbol_rate = 23.6
    num_tones = 16                      # This particular MFSK modulation contains 16 tones i.e. (500-100/23.6) =~ 16.95  
                                        # But its apparently odd to have an odd number of frequencies
                                        # So, I settled on '16'. Turns out that was right. 
    tone_zero = int(round(base_freq/symbol_rate))       # the first or lowest tone in the sequence 

    sample_rate = 48000
    nyq_rate = sample_rate / 2.0
    order = 9                          # This number is after experimentation. like Filter-design always is
    cutoff = 560                       # same as above.

    for index in iter(peaks):
        despread_re = np.multiply(upsampled_signal, re[ index[0]  : index[0] + len(upsampled_signal) ])
        despread_im = np.multiply(upsampled_signal, im[ index[0]  : index[0] + len(upsampled_signal) ])

        normal_cutoff = cutoff / nyq_rate
        # Get the filter coefficients 
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        real = filtfilt(b, a, despread_re)
        
        normal_cutoff = cutoff / nyq_rate
        # Get the filter coefficients 
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        imag = filtfilt(b, a, despread_im)

        
        fft_instant_real = np.fft.rfft(real)
        real_fft = fft_instant_real[tone_zero : tone_zero + num_tones]
            
        fft_instant_imag = np.fft.rfft(imag)
        imag_fft = fft_instant_imag[tone_zero : tone_zero + num_tones]
        

        currsymbol = np.argmax(np.absolute(real_fft))
        symbols_real.append(currsymbol)
        
        currsymbol = np.argmax(np.absolute(imag_fft))
        symbols_imag.append(currsymbol)

        return symbols_real, symbols_imag