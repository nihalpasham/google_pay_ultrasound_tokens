
import numpy as np
from symbol_decode import symbol_decode
from load_wavfile import load_wavfile

base_freq = 94.5
symbol_rate = 23.44
num_tones = 16
tone_zero = int(round(base_freq/symbol_rate))

symbols = symbol_decode()
re, im, _, _ = load_wavfile()

def symbol_selector(pos):
    
    symbol = []
    symbol_holder = []
    symbol_decode = np.zeros(shape=(16,14))
    symbol_final =[]
    symbol_position = pos

    for i in range(0, len(symbols)-10):
        if symbols[i] == 15:
            symbol.append(i+symbol_position)
#             print(symbol)

#     symbol.remove(190)
    print(len(symbol))

    for i in iter(symbol):
        index = i*127
        
        despread_re =  re[ index  : index + 127 ]
        despread_im =  im[ index  : index + 127 ]
#         print(len(despread_re))
#         print(len(despread_im))

        complex_signal = []

        for i in range(0, len(despread_re)):
            complex_signal.append(np.complex(despread_re[i], despread_im[i]))

        fft_instant = np.fft.fft(complex_signal)
        fft_instant = fft_instant[tone_zero : tone_zero + num_tones]
        symbol_holder.append(np.absolute(fft_instant))

    print(len(symbol_holder))
    symbol_holder = symbol_holder[:14]   # across 14 token iterations

    for i in range(0, len(symbol_holder)):
        symbol_decode[:,i] = symbol_holder[i]

    for i in range(0, len(symbol_decode)):
        symbol_final.append(sum(symbol_decode[i]))

    print(symbol_final)
    print(np.argmax(symbol_final))
    
symbol_selector(8)
