import numpy as np
import matplotlib.pyplot as plt

# --- Create a sphere ---
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))

# Flatten points into (N,3)
points = np.vstack((x.flatten(), y.flatten(), z.flatten()))

# --- Transformation Matrices ---

# Scaling matrix
S = np.diag([1.5, 1, 0.5])

# Rotation about Z-axis (45 degrees)
theta = np.pi / 4
Rz = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta),  np.cos(theta), 0],
    [0, 0, 1]
])

# Translation vector
T = np.array([[2], [1], [0]])

# --- Apply transformations ---
# 1. Scale
scaled = S @ points
# 2. Rotate
rotated = Rz @ scaled
# 3. Translate
translated = rotated + T

# Reshape back to meshgrid form
x_new = translated[0, :].reshape(x.shape)
y_new = translated[1, :].reshape(y.shape)
z_new = translated[2, :].reshape(z.shape)

# --- Plot results ---
fig = plt.figure(figsize=(10,5))

ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(x, y, z, color="cyan", alpha=0.6)
ax.set_title("Original Sphere")

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x_new, y_new, z_new, color="green", alpha=0.7)
ax2.set_title("Scaled + Rotated + Translated")

plt.show()
