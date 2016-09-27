# Setup a layer
layer = PointGrid(area, 500, (25, 25))
solver = (EQLGravity(x, y, z, gz, layer) +
          10**-24*Damping(layer.size)).fit()
# Check that the predicted data fits the observations
np.allclose(gz, solver[0].predicted(), rtol=0.01, atol=0.5)
# True
# Add the densities to the layer
layer.addprop('density', solver.estimate_)
# Make a regular grid
x, y, z = gridder.regular(area, (30, 30), z=-1)
# Interpolate and check against the model
gz_layer = sphere.gz(x, y, z, layer)
gz_model = prism.gz(x, y, z, model)
np.allclose(gz_layer, gz_model, rtol=0.01, atol=0.5)
# True
# Upward continue and check against model data
zup = z - 500
gz_layer_up = sphere.gz(x, y, zup, layer)
gz_model_up = prism.gz(x, y, zup, model)
np.allclose(gz_layer_up, gz_model_up, rtol=0.01, atol=0.1)
# True
# Plot the interpolated and upward continued data
plt.close()
fig = plt.figure(figsize=(6, 5))
_ = plt.tricontourf(y, x, gz_layer_up, 30, cmap='Reds')
plt.colorbar(pad=0, aspect=30).set_label('mGal')
