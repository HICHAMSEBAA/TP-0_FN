import numpy as np
import matplotlib.pyplot as plt

# Paramètres du signal
A = 1.5
F = 60 # Hz

# Paramètres d'échantillonnage
Fe = 1000 # Hz
duree = 0.5 # s
N = int(duree * Fe) # Nombre de points d'échantillonnage
t = np.arange(N) / Fe # Axe temporel

# Génération du signal
x = A * np.cos(2 * np.pi * F * t)
plt.figure(1)
# Tracé du signal
plt.plot(t, x)
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')


# Calcul du spectre d'amplitude
X = np.abs(np.fft.fft(x))
plt.figure(2)
# Tracé du spectre d'amplitude
freq = np.fft.fftfreq(N, 1/Fe)
plt.plot(freq, X)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Amplitude')


# Calcul du spectre centré sur zéro
X_shifted = np.fft.fftshift(X)
freq_shifted = np.fft.fftshift(freq)
plt.figure(3)
# Tracé du spectre centré sur zéro
plt.plot(freq_shifted, X_shifted)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('Amplitude')
plt.show()
