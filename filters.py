import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from numpy import asarray
from numpy import savetxt

# Load the signals data
data = np.loadtxt('ID_AH_Movement_1.txt')
t = data[:, 0]
signals = data[:, 1:]
#print(t)
#print(signals)

# Define the sampling frequency
fs = 1 / (t[1] - t[0])

# Design the Bandpass filter
b1, a1 = signal.butter(4, 10/(fs/2), 'highpass') #butterworth
b2, a2 = signal.butter(4, [15, 35], 'bandpass', fs=fs) #bandpass

# Apply the filters to each signal
filtered_signals = np.zeros_like(signals)
for i in range(signals.shape[1]):
    filtered_signals[:, i] = signal.filtfilt(b1, a1, signals[:, i]) #butterworth
    filtered_signals[:, i] = signal.lfilter(b2, a2, filtered_signals[:, i]) #bandpass
    filtered_signals[:, i] = np.abs(filtered_signals[:, i])
    data_min = min(filtered_signals[:,i])
    data_max = max(filtered_signals[:, i])
    filtered_signals[:, i] = (filtered_signals[:, i] - data_min)/(data_max - data_min)

# Plot the original and filtered signals
plt.figure()
#plt.plot(t, signals, color = 'b')
plt.plot(t, filtered_signals, color = 'g')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [mV]')
plt.savefig("AH1_filtered")

#save to csv file
df = pd.DataFrame(filtered_signals, index = None)
df.insert(0, "seconds", t)
df.to_csv("AH1_filtered.csv", index = False)
#data = asarray(filtered_signals)
