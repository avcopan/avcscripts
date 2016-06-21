from avcscripts.plotter import PlotData
import matplotlib.pyplot as plt

# define some variables
hartree2kcal = 627.509469
palette = {
  'black'    :'#000000', # black
  'dark blue':'#16469D', # dark blue
  'red'      :'#BD202D', # red
  'green'    :'#00A14B', # green
  'blue'     :'#4B96D1', # light blue
  'orange'   :'#F16521', # orange
  'violet'   :'#9F6EAF' # light purple
}
color_cycle = [palette['red'], palette['blue'], palette['orange'], palette['green']]
label_cycle = ['CCSDT', 'CCSDT(Q)', 'ODC-12', 'L-ODC$\lambda_3$']

# build PlotData object
plotdata_obj = PlotData.init_from_file('data.txt')
plotdata_obj.set_reference_series(0) # set 0th column as reference, so the data series are now differences with respect to column 0
plotdata_obj.scale_y(hartree2kcal)   # convert vertical axis from Hartree to kcal mol
plotdata_obj.set_color_cycle(color_cycle, label_cycle=label_cycle)
plotdata_obj.plot_all('-', linewidth=3.0)
plotdata_obj.set_aspect_by_adjusting_width(1.8)

#  matplotlib stuff
plt.rc('text', usetex=True)
plt.rc('font', family='serif', weight='bold', size=20)
plt.margins(y=0.05, x=0.00, tight=True)
plt.ylabel('$\Delta E$ / kcal mol$^{-1}$')
plt.xlabel('$r$ / \AA')
plt.tight_layout()
plt.legend(loc='lower left')
plt.savefig('data.pdf', bbox_inches='tight')


