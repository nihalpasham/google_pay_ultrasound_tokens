
from scipy.fftpack import fft, fftfreq, fftshift
from scipy import signal
from scipy.signal import butter,filtfilt
import matplotlib.pyplot as plt
import numpy as np
from code_signal import code_construct
from code_tracking import code_tracking
from load_wavfile import load_wavfile


k = 'refer to the jupyter notebook for more info'                               # one of the peaks chosen randomly 
sample_rate = 48000
nyq_rate = sample_rate / 2.0
order = 9
cutoff = 560

path_to_file = 'some input wav file'
upsampled_signal = code_construct()
re, im, _, _ = load_wavfile(path_to_file)


despread_re = np.multiply(upsampled_signal, re[ k  : k + len(upsampled_signal) ])
despread_im = np.multiply(upsampled_signal, im[ k  : k + len(upsampled_signal) ])

# Apply a low pass filter with the cut-off at 560 hz seems to work well.
normal_cutoff = cutoff / nyq_rate
# Get the filter coefficients 
b, a = butter(order, normal_cutoff, btype='low', analog=False)
y = filtfilt(b, a, despread_re)

f = signal.resample(y, 512)

N = 512
# sample spacing
T = 1.0 / 12000.0
yf = fft(f)
xf = fftfreq(N, T)
xf = fftshift(xf)
yplot = fftshift(yf)

plt.figure(figsize=(30,10))
plt.plot(xf, 1.0/N * np.abs(yplot))
plt.xticks(np.arange(min(xf), max(xf)+1, 500.0))
plt.grid()
plt.show()
