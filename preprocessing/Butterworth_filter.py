from scipy.signal import butter, filtfilt
import numpy as np
import matplotlib.pyplot as plt
from numpy import asarray
from numpy import savetxt
import csv

def butterworth_filter(signal, fs, cutoff, order):
    b, a = butter(order, cutoff/(fs/2), 'highpass')
    filtered_signal = filtfilt(b, a, signal)
    return filtered_signal
data = np.loadtxt('ID_AV Movement 2.txt')



signals = data[:, 1:]
filtered_data = np.zeros_like(data)
filtered_data[:,0] = data[:, 0]
for i in range(1,10):
    signal = data[:, i]
    fs = len(data)/data[len(data)-1][0]
    cutoff = 10 # cutoff frequency
    order = 4 # order of the filter
    filtered_signal = butterworth_filter(signal, fs, cutoff, order)
    filtered_data[:, i] = filtered_signal



# save to csv file
savetxt('AV_1_Butterworth_filtered.csv', filtered_data, delimiter=',')

data = np.loadtxt('ID_AV Movement 2.txt')
i = 1

while i <= 9:
    plt.plot(data[:,0], data[:,i], color = 'g',label = "AV_2_" + str(i) +  " Data")
    plt.plot(filtered_data[:,0], filtered_data[:,i], color = 'b',label = "AV_2_" + str(i) +  " Data")
    plt.xlabel("Seconds")
    plt.ylabel("MilliVoltage")
    plt.savefig("AV2_" + str(i))
    i += 1