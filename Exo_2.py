import numpy as np
import matplotlib.pyplot as plt
import array

plt.figure(1)
N = 16
n = np.arange(N)

#
xn = np.ones(N)
plt.subplot(3,1,1)
plt.stem(n, xn, 'r-', label='signal (xn) ')
plt.xlabel('N')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

#
plt.figure(2)
nf1 = n/N
xf1 = np.fft.fft(xn)
xf1c = np.fft.fftshift(xf1)
#plt.subplot(3,1,1)
#plt.plot(nf1, np.abs(xf1), 'b-', label='signal TF[xn]')
plt.xlabel('N')
plt.ylabel('TF[xn]')
plt.legend()
plt.grid(True)

#
plt.figure(2)
axe_f = np.arange(-1/2, 0.5, 1/N)
plt.subplot(3,1,1)
plt.plot(axe_f, np.abs(xf1c), 'r-', label='signal TFc[xn]')
plt.xlabel('f (Hz)')
plt.ylabel('TFc[xn]')
plt.legend()
plt.grid(True)

#
plt.figure(1)
xn2 = np.zeros(48)
for i in range(N):
    xn2.put(i, 1)
n2 = np.arange(48)
plt.subplot(3,1,2)
plt.stem(n2, xn2, 'b-', label='signal (xn1) ')
plt.xlabel('N')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

#
plt.figure(2)
xf2 = np.fft.fft(xn2)
xf2c = np.fft.fftshift(xf2)
axe_f = np.arange(-1/2, 0.5, 1/48)
plt.subplot(3,1,2)
plt.plot(axe_f, np.abs(xf2c), 'b-', label='signal TFc2[xn]')
plt.xlabel('f (Hz)')
plt.ylabel('TFc2[xn]')
plt.legend()
plt.grid(True)

#
plt.figure(1)
xn3 = np.zeros(128)
for i in range(N):
    xn3.put(i, 1)
n3 = np.arange(128)
plt.subplot(3,1,3)
plt.stem(n3, xn3, 'g-', label='signal (xn2) ')
plt.xlabel('N')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

#
plt.figure(2)
xf3 = np.fft.fft(xn3)
xf3c = np.fft.fftshift(xf3)
axe_f = np.arange(-0.5, 0.5, 1/128)
plt.subplot(3,1,3)
plt.plot(axe_f, np.abs(xf3c), 'g-', label='signal TFc3[xn]')
plt.xlabel('f (Hz)')
plt.ylabel('TFc3[xn]')
plt.legend()
plt.grid(True)
plt.show()


