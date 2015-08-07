import numpy as np
from avcscripts.parser  import ParseFile
from avcscripts.plotter import PlotData

pfile = ParseFile('filestoparse/qchem_eom-ee.out')
energies  = pfile.findfloats(r'Excitation energy = (-?\d+.\d+) eV.')
distances = pfile.findfloats(r'H \(  1\)\n\s+ H \(  2\)\s+(\d+\.\d+)')

energies  = energies.reshape((-1,2,12)).transpose(1,2,0)

singlets  = PlotData(distances, energies[0])
triplets  = PlotData(distances, energies[1])

singlets.save_to_file('plotdatafiles/h2singlets.dat', floatfmt='%10.5f')
triplets.save_to_file('plotdatafiles/h2triplets.dat', floatfmt='%10.5f')

obj = PlotData.load_from_file('plotdatafiles/h2singlets.dat')
print obj.points
print obj.dataseries
