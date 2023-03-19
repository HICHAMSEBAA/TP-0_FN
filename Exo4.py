import numpy as np
import matplotlib.pyplot as plt

# use of functions to define signals of particular shapes
f = 60  # frequency in Hz
fe = 1000
Te = 1/1000  # sampling period in seconds
t = np.arange(0, 0.5, Te)  # time vector
c = 0.5j
w = 4 * np.pi * f# angular frequency in radians/second

signal = np.exp(c*w*t)

plt.figure(1)

#
plt.subplot(3,1,1)
plt.plot(t, signal, 'r-', label='Exp(t) ')
plt.xlabel('t (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

#
plt.subplot(3,1,2)
plt.plot(t, np.real(signal), label='Partie réelle')
plt.xlabel('t (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

#
plt.subplot(3,1,3)
plt.plot(t, np.imag(signal), 'g-', label='Partie imaginaire')
plt.xlabel('t (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

#
plt.figure(2)
plt.subplot(3,1,1)
plt.stem(t, signal, 'b-', label='Exp(nTe) ')
plt.xlabel('t (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

#
plt.subplot(3,1,2)
TF = np.fft.fft(signal)
plt.stem(t, np.abs(TF), 'g-', label='TF[Exp(t)] ')
plt.xlabel('f (Hz)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

#
plt.subplot(3,1,3)
TFc = np.fft.fftshift(TF)
freqs = np.fft.fftfreq(len(signal), d=Te)
freqs_shifted = np.fft.fftshift(freqs)
plt.plot(freqs_shifted, np.abs(TFc), 'y-', label='TFc[Exp(t)] ')
plt.xlabel('f (Hz)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()