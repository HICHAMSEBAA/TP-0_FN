import numpy as np
import matplotlib.pyplot as plt

# use of functions to define signals of particular shapes
f = 60  # frequency in Hz
fe = 1000
Te = 1/fe  # sampling period in seconds
A = 1.5
t = np.arange(0, 0.5, Te)  # time vector
w = 2 * np.pi * f# angular frequency in radians/second

signal = A*np.cos(w*t)

plt.figure(1)

#
plt.subplot(3,1,1)
plt.plot(t, signal, 'r-', label='cos(w*t) ')
plt.xlabel('t (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

#
plt.subplot(3,1,2)
TF = np.fft.fft(signal)
plt.stem(t, np.abs(TF), 'g-', label='TF[cos(w*t)] ')
plt.xlabel('f (Hz)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

#
plt.subplot(3,1,3)
TFc = np.fft.fftshift(TF)
freqs = np.fft.fftfreq(len(signal), d=Te)
freqs_shifted = np.fft.fftshift(freqs)
plt.plot(freqs_shifted, np.abs(TFc), 'y-', label='TFc[cos(w*t)] ')
plt.xlabel('f (Hz)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()