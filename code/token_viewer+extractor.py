
from symbol_decode import symbol_decode 
import numpy as np
from code_signal import code_construct
from code_tracking import code_tracking
from load_wavfile import load_wavfile

path_to_file = 'your input wav file'
first_peak_index =  'look it up'                # refer to the example in the jupyter notebook

upsampled_signal = code_construct()
re, im, _, _ = load_wavfile(path_to_file)
peaks = code_tracking(first_peak_index)
symbols_real, symbols_imag = symbol_decode(peaks, upsampled_signal, re, im)


def token_viewer():

    tokens_real = []
    tokens_imag = []
    
    for i in range(0, len(symbols_real)-1):
        if symbols_real[i] == 15:
            token = symbols_real[i:i+8]
            tokens_real.append(token)
            
    for i in range(0, len(symbols_imag)-1):
        if symbols_imag[i] == 15:
            token = symbols_imag[i:i+8]
            tokens_imag.append(token)
            
    print(tokens_real)
    print(tokens_imag)


def final_token_extractor():

    real_tokens = []
    imag_tokens = []

    for i in range(0, len(symbols_real)):
        if symbols_real[i] == 15:
            token = symbols_real[i:i+8]
            checksum = np.sum(token) % 16
            if checksum <= 4 or checksum >= 13 :
                q = (''.join([format(symbol, 'x') for symbol in token[1:7]]))
    #             print(q)
    #             print(int(q, 16))
                real_tokens.append(int(q, 16))

    for i in range(0, len(symbols_imag)):
        if symbols_imag[i] == 15:
            token = symbols_imag[i:i+8]
            checksum = np.sum(token) % 16
            if checksum <= 4 or checksum >= 13 :
                q = (''.join([format(symbol, 'x') for symbol in token[1:7]]))
    #             print(q)
    #             print(int(q, 16))
                imag_tokens.append(int(q, 16))
                
    def remove_duplicates(token_list): 
        final_list = [] 
        for num in token_list: 
            if num not in final_list: 
                final_list.append(num) 
        return final_list 

    print(remove_duplicates(real_tokens))
    print(remove_duplicates(imag_tokens))
