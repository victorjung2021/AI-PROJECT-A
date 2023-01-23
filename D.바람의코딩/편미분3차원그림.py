# 편미분
# f(x0,x1) = x0**2 + x1**2
import matplotlib as plt
import numpy as np

def function_2(x):
  return x[0]**2 + x[1]**2

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# Grab some test data.
# X, Y, Z = axes3d.get_test_data(0.05)
X = np.arange(-3.0, 3.0, 0.05)
Y = np.arange(-3.0, 3.0, 0.05)
X, Y = np.meshgrid(X, Y)
Z = X**2 + Y**2

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()