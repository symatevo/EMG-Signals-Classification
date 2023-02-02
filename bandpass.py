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
b, a = signal.butter(4, [15, 35], 'bandpass', fs=fs)

# Apply the Bandpass filter to each signal
filtered_signals = np.zeros_like(signals)
for i in range(signals.shape[1]):
    filtered_signals[:, i] = signal.lfilter(b, a, signals[:, i])

print("hesa")
print(filtered_signals)
# Plot the original and filtered signals
plt.figure()
plt.plot(t, signals, color = 'b', label='Original signals')
plt.plot(t, filtered_signals, color = 'g', label='Filtered signals')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [mV]')
plt.legend()
plt.savefig("bandpassed")

#save to csv file
df = pd.DataFrame(filtered_signals, index = None)
df.insert(0, "seconds", t)
df.to_csv("AH1_bandpass_filtered.csv", index = False)
#data = asarray(filtered_signals)
