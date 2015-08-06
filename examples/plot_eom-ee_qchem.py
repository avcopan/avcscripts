from avcscripts.plotter import PlotData

sngdata = PlotData('singlets.dat', transpose=True)
print sngdata.points
print sngdata.dataseries
#print sngdata.keys
#print sngdata.labels

import matplotlib.pyplot as pp

sngdata.plot_all('b-')
pp.savefig('singlets.pdf')

