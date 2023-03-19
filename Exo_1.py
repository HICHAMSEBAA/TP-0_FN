import numpy as np
import matplotlib.pyplot as plt

# Define the time interval and sampling period
Te = 1 # s
t = np.arange(-20*Te, 30*Te + Te, Te)

# Define the unit impulse function
delta = np.zeros_like(t)
delta[t == 0] = 1
print(delta)

# a delayed unit pulse of 11
delta1 = np.zeros_like(t)
delta1[t == 11] = 1

# an advanced unit pulse of 8
delta2 = np.zeros_like(t)
delta2[t == -8] = 1

# Create a new figure with ID 1
plt.figure(2)

# Turn on the grid lines
plt.grid(True)

# Plot the unit impulse
plt.stem(t, delta, 'r-', label='unit impulse')
plt.stem(t, delta1, 'b-', label='a delayed unit pulse of 11')
plt.stem(t, delta2, 'g-', label='an advanced unit pulse of 8')

# Customize the plot
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Unit Impulse')
plt.legend()

# Show the plot
plt.show()
