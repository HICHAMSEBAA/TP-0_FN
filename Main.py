import numpy as np
import statistics as st
import matplotlib.pyplot as plt

# The creation of a set of n equidistant points and uniformly distributed between two points a and b
a = 1    # start value
b = 10   # end value
n = 10   # number of values to generate
v = np.linspace(a, b, n)
print(type(v))
print(v)

# use of functions to define signals of particular shapes
one = np.ones((3,2))
zero = np.zeros((3,3))
f = 1.0  # frequency in Hz
Te = 0.01  # sampling period in seconds
t = np.arange(0, 1, Te)  # time vector
w = 2 * np.pi * 2.0  # angular frequency in radians/second

p = np.sin(2 * np.pi * f * Te * t)
print(p)
q = 5 * np.cos(w * t)
print(q)
s = np.exp(1j * 2 * np.pi * f * Te * t)
print(s)


# mean
mean = st.mean(v)
print(mean)





# Transformation des signaux numériques X = fft (x) ;
X = np.fft.fft(v)
print(X)
X_r = np.real(X)
print(X_r)
X_i = np.imag(X)
print(X_i)

# Module
X_module = np.abs(X)
print(X_module)

# Phase
X_phase = np.angle(X)
print(X_phase)

# To have correctly centered representations of the module and phase, two orders can be introduced
X_shifted = np.fft.fftshift(X)
Xm_c = np.abs(X_shifted)
Xph_c = np.unwrap(np.angle(X_shifted))


# Moving up from frequency space to time space (spatial), is achieved by applying the reverse Fourier transform
x = np.fft.ifft(X)

# To plot a signal

plt.plot(t, p)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sinusoidal signal')

# Turn on the grid lines
plt.grid(True)

# Plot multiple curves on the same plot
plt.plot(t, p, 'r-', label='sine')
plt.plot(t, q, 'b-', label='cosine')
plt.xlabel('Angle (radians)')
plt.ylabel('Amplitude')
plt.title('Trigonometric Functions')
plt.legend()
plt.show()

# Create a scatter plot with custom markers and colors
x = np.random.normal(size=100)
y = np.random.normal(size=100)
colors = np.random.rand(100)
sizes = 100 * np.random.rand(100)
plt.scatter(x, y, c=colors, s=sizes, marker='o', alpha=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Random Scatter Plot')
#plt.show()

# Create a grid of subplots
plt.subplot(2, 1, 1)
plt.plot(x, p, 'r-', label='sine')
plt.xlabel('Angle (radians)')
plt.ylabel('Amplitude')
plt.title('Trigonometric Functions')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x, q, 'g--', label='cosine')
plt.xlabel('Angle (radians)')
plt.ylabel('Amplitude')
plt.legend()
#plt.show()