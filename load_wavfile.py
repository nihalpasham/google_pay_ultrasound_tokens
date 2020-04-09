import numpy as np
import os
from scipy.io import wavfile
import matplotlib.pyplot as plt


def load_wavfile():
    
    re = []
    im = []

    file_path = "Your input wav file"

    fs, data = wavfile.read(file_path)

    print(fs)

    if(data.dtype == np.int16):
        data = data.astype(np.float)/2**16
        
    data_shape = data.shape[0]
    # print(len(data))

    re, im = np.hsplit(data, 2)

    re = np.multiply(re.reshape(data.shape[0],), 1e+02)
    im = np.multiply(im.reshape(data.shape[0],), 1e+02)

    number_of_complex_samples = len(data)

    plt.figure(figsize=(20,10))
    plt.plot((re))
    plt.plot(im)
    # label the axes
    plt.ylabel("Amplitude")
    plt.xlabel("Time (samples)")
    # set the title
    plt.title("Samples")
    # display the plot
    plt.show()

    return re, im, number_of_complex_samples, data_shape