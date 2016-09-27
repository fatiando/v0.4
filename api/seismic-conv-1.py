import numpy as np
import matplotlib.pyplot as plt
from fatiando.seismic import conv
from fatiando.vis import mpl
# Choose some velocity depth model
n_samples, n_traces = [600, 20]
rock_grid = 1500.*np.ones((n_samples, n_traces))
rock_grid[300:, :] = 2500.
# Convert from depth to time
vel_l = conv.depth_2_time(rock_grid, rock_grid, dt=2.e-3, dz=1.)
# Considering rho constant
rho_l = np.ones(np.shape(vel_l))
# Calculate the reflectivity for all the model
rc = conv.reflectivity(vel_l, rho_l)
# Convolve the reflectivity with a ricker wavelet
synt = conv.convolutional_model(rc, 30., conv.rickerwave, dt=2.e-3)
# Plot the result
fig = plt.figure(figsize=(6,5))
_ = mpl.seismic_wiggle(synt, dt=2.e-3)
_ = mpl.seismic_image(synt, dt=2.e-3,
                           cmap=mpl.pyplot.cm.jet, aspect='auto')
_ = plt.ylabel('time (seconds)')
_ = plt.title("Convolutional seismogram", fontsize=13,
              family='sans-serif')
