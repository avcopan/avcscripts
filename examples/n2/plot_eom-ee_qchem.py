from avcscripts.plotter import PlotData

singlets = PlotData.init_from_file('plotdatafiles/n2singlets.dat')
triplets = PlotData.init_from_file('plotdatafiles/n2triplets.dat')

import matplotlib.pyplot as pp

singlets.plot_all('b-')
pp.savefig('singlets.pdf')
triplets.plot_all('b-')
pp.savefig('triplets.pdf')

