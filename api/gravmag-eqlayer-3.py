x1, y1, z1 = gridder.scatter(area, 200, z=-400, seed=0)
gz = prism.gz(x1, y1, z1, model)
x2, y2, z2 = gridder.scatter(area, 400, z=-150, seed=2)
gxy = prism.gxy(x2, y2, z2, model)
# Plot the gz and gxy data
plt.close()
fig = plt.figure(figsize=(12, 5))
ax = plt.subplot(121, aspect='equal')
_ = plt.title('gz')
_ = plt.tricontourf(y1, x1, gz, 30, cmap='Reds')
plt.colorbar(pad=0, aspect=30).set_label('mGal')
_ = plt.plot(y1, x1, '.k')
ax = plt.subplot(122)
_ = plt.title('gxy')
_ = plt.tricontourf(y2, x2, gxy, 30, cmap='RdBu_r')
plt.colorbar(pad=0, aspect=30).set_label('Eotvos')
_ = plt.plot(y2, x2, '.k')
plt.tight_layout()
