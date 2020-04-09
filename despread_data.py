import struct
import numpy as np
from code_signal import code_construct
from code_tracking import code_tracking
from load_wavfile import load_wavfile

path_to_file = 'your input wav file'
iq_file_path = "your output filename"
iq_file = open(iq_file_path, 'wb')
first_peak_index = 'find it via visual inspection'  # refer to the jupyter notebook for more info.

upsampled_signal = code_construct()
re, im, number_of_complex_samples, _ = load_wavfile(path_to_file)

peaks = code_tracking(first_peak_index, upsampled_signal, re, im)

# for i in range(0, COMPLEX_SIZE * 1000):
#     real_data_write = struct.pack('@f', 0)
#     iq_file.write(real_data_write)
#     imag_data_write = struct.pack('@f', 0)
#     iq_file.write(imag_data_write)

for i in iter(peaks):
    despread_re = np.multiply(upsampled_signal, re[ i[0]  : i[0] + len(upsampled_signal) ])
    despread_im = np.multiply(upsampled_signal, im[ i[0]  : i[0] + len(upsampled_signal) ])

    for j in range(0, len(despread_re)):
        real_data_write = struct.pack('@f', despread_re[j])
        iq_file.write(real_data_write)
        imag_data_write = struct.pack('@f', despread_im[j])
        iq_file.write(imag_data_write)

iq_file.close()
print('done')