# Setup a layer
layer = PointGrid(area, 500, (25, 25))
solver = (EQLGravity(x1, y1, z1, gz, layer, field='gz') +
          EQLGravity(x2, y2, z2, gxy, layer, field='gxy') +
          10**-24*Damping(layer.size)).fit()
# Check the fit
gz_pred = solver[0].predicted()
gxy_pred = solver[1].predicted()
np.allclose(gz, gz_pred, rtol=0.01, atol=0.5)
# True
np.allclose(gxy, gxy_pred, rtol=0.01, atol=0.5)
# True
# Add the densities to the layer
layer.addprop('density', solver.estimate_)
