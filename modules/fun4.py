import matplotlib.pyplot as plt
import numpy as np

# 1. Generate x values
# Create 400 points between -2π and 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

# 2. Calculate y values
y_sin = np.sin(x)
y_cos = np.cos(x)

# 3. Create the plot
plt.figure(figsize=(10, 6))  # Set the figure size (width, height)

# Plot Sine
plt.plot(x, y_sin, label='sin(x)', color='blue', linewidth=2)

# Plot Cosine
plt.plot(x, y_cos, label='cos(x)', color='red', linestyle='--', linewidth=2)

# 4. Customize the chart
plt.title('Trigonometric Functions: Sine and Cosine')
plt.xlabel('Angle (radians)')
plt.ylabel('Amplitude')

# Add a grid for easier reading
plt.grid(True, which='both', linestyle=':', alpha=0.6)

# Add a horizontal line at y=0 (the x-axis)
plt.axhline(y=0, color='black', linewidth=1)

# Add the legend (uses the 'label' arguments from plt.plot)
plt.legend()

# 5. Display the plot
plt.show()