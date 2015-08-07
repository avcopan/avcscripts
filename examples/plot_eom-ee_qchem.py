from avcscripts.plotter import DataPlotter

plotter = DataPlotter('plotdatafiles/h2singlets.dat')
print plotter.points
print plotter.dataseries
#print plotter.keys
#print plotter.labels

import matplotlib.pyplot as pp

plotter.plot_all('b-')
pp.savefig('singlets.pdf')

