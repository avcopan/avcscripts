from avcscripts.plotter import PlotData

singlets = PlotData.init_from_file('plotdatafiles/h2singlets.dat')
print singlets.points
print singlets.dataseries
#print singlets.keys
#print singlets.labels

import matplotlib
import matplotlib.pyplot as pp

matplotlib.rc('font', family='sans-serif') 
matplotlib.rc('font', serif='Helvetica') 
matplotlib.rc('text', usetex='false') 
singlets.plot_all('b-')
pp.savefig('singlets.pdf')

