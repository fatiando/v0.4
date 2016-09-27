# Upward continue gxy only without interpolation
zup = z2 - 500
gxy_layer = sphere.gxy(x2, y2, zup, layer)
# Check against model data
gxy_model = prism.gxy(x2, y2, zup, model)
np.allclose(gxy_layer, gxy_model, rtol=0.01, atol=0.5)
# True
# Plot the upward continued gxy
plt.close()
fig = plt.figure(figsize=(6, 5))
_ = plt.title('Upward continued gxy')
_ = plt.tricontourf(y2, x2, gxy_layer, 30, cmap='RdBu_r')
plt.colorbar(pad=0, aspect=30).set_label('Eotvos')
_ = plt.plot(y2, x2, '.k')
