import numpy as np
import matplotlib.pyplot as plt
from fatiando import gridder
from fatiando.gravmag import sphere, prism
from fatiando.gravmag.eqlayer import EQLGravity
from fatiando.mesher import Prism, PointGrid
from fatiando.inversion.regularization import Damping
# Produce some gravity data
area = (0, 10000, 0, 10000)
x, y, z = gridder.scatter(area, 500, z=-1, seed=0)
model = [Prism(4500, 5500, 4500, 5500, 200, 5000,
               {'density': 1000})]
gz = prism.gz(x, y, z, model)
# Plot the data
fig = plt.figure(figsize=(6, 5))
_ = plt.tricontourf(y, x, gz, 30, cmap='Reds')
plt.colorbar(pad=0, aspect=30).set_label('mGal')
_ = plt.plot(y, x, '.k')
