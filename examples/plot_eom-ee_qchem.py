from avcscripts.plotter import PlotData

singlets = PlotData.init_from_file('plotdatafiles/h2singlets.dat')
print singlets.points
print singlets.dataseries
#print singlets.keys
#print singlets.labels

import matplotlib.pyplot as pp

singlets.plot_all('b-')
pp.savefig('singlets.pdf')

