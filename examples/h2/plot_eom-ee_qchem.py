from avcscripts.plotter import PlotData

singlets = PlotData.init_from_file('plotdatafiles/h2singlets.dat')

import matplotlib.pyplot as pp

singlets.plot_all('b-')
pp.savefig('singlets.pdf')

