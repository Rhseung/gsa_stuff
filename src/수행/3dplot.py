import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(0, 1.01, 0.01)
Y = np.arange(0, 1.01, 0.01)
X, Y = np.meshgrid(X, Y)
Z = 1-X-Y

ax.set_zlim(0, 1.01)
# Plot the surface.
surf = ax.plot_surface(X, Y, Z)

# # Customize the z axis.
# ax.zaxis.set_major_locator(LinearLocator(10))
# # A StrMethodFormatter is used automatically
# ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
# fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()