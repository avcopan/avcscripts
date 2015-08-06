import numpy as np
from avcscripts.parser  import ParseFile

pfile = ParseFile('qchem_eom-ee.out')
energies  = pfile.findfloats(r'Excitation energy = (-?\d+.\d+) eV.')
distances = pfile.findfloats(r'H \(  1\)\n\s+ H \(  2\)\s+(\d+\.\d+)')

energies  = energies.reshape((-1,2,12)).transpose(1,0,2)
distances = distances.reshape(-1,1)
print energies[1].shape
print distances.shape
singlets  = np.append(distances, energies[0], axis=1)
triplets  = np.append(distances, energies[1], axis=1)

snglabels = [('s{:d}'.format(i),'$S_{{{:d}}}$'.format(i)) for i in range(1,13)]
print snglabels
np.savetxt('singlets.dat', singlets, fmt='%10.5f')
np.savetxt('triplets.dat', triplets, fmt='%10.5f')

