
'''
This script averages FFT scores across 14 tokens. 
This idea is to aggregate FFT scores for each token and look at the one's with the max score. This way the probability that we'd
find the right symbol is higher.
So, instead of looking at one token, we look at 14 tokens before we decide on the symbol.  
'''
import numpy as np
from symbol_decode import symbol_decode
from load_wavfile import load_wavfile
from code_tracking import code_tracking 
from code_correlation import code_correlate
from code_signal import code_construct

base_freq = 94.5
symbol_rate = 23.44
num_tones = 16
tone_zero = int(round(base_freq/symbol_rate))

path_to_file = 'your filtered input wav file'
first_peak_index ='you will to find this one manually'    # refer to the jupyter notebook for details

upsampled_signal = code_construct()
symbols_real, symbols_imag = symbol_decode()
re, im, _, _ = load_wavfile(path_to_file)
peaks = code_tracking(first_peak_index, upsampled_signal, re, im)

def symbol_selector(pos):
    
    symbol = []
    symbol_holder = []
    symbol_decode = np.zeros(shape=(16,14))
    symbol_final =[]
    symbol_position = pos

    for i in range(0, len(symbols_real)-10):
        if symbols_real[i] == 15:
            symbol.append(i+symbol_position)
#             print(symbol)

#     symbol.remove(190)
    print(len(symbol))

    for i in iter(symbol):
        index = peaks[i]

        despread_re = np.multiply(upsampled_signal, re[ index[0]  : index[0] + len(upsampled_signal) ])
        despread_im = np.multiply(upsampled_signal, im[ index[0]  : index[0] + len(upsampled_signal) ])

        fft_instant = np.fft.rfft(despread_re)                       # you could swap this with 'despread_im' 
                                                                    # if you want to check for symbol avgs in the 
                                                                    # imaginary component of the signal
        fft_instant = fft_instant[tone_zero : tone_zero + num_tones]
        symbol_holder.append(np.absolute(fft_instant))

    #print(len(symbol_holder))
    symbol_holder = symbol_holder[:14]     # lets limit our ourselves to a max of 14 token iterations

    for i in range(0, len(symbol_holder)):
        symbol_decode[:,i] = symbol_holder[i]
#     print(symbol_decode)
    for i in range(0, len(symbol_decode)):
        symbol_final.append(sum(symbol_decode[i]))

    print(symbol_final)
    print(np.argmax(symbol_final))
    
symbol_selector(3)

'''
Example output:

Final aggregate FFT scores across 14 token repetitions for position 3 >> 
[5.004761852654423, 5.082920561378226, 4.689137960986634, 3.3774743811253702, 
 6.524294520223517, 10.295328866096405, 5.09305752986283, 3.0088793232694986, 
 7.896026254298636, 4.7476164850763105, 4.578212634036975, 6.96808189763428, 
 5.426906602680647, 8.35283363790876, 3.972977040984497, 2.1006219981671257]

Highest score is the most probable symbol >> 5
'''
