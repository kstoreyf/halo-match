import numpy as np
from Corrfunc.theory.xi import xi

import utils


tag = '_abacus_small_rbig'
halos, arrs = utils.load_halos(tag, cols=['x','y','z'], subsample=1000)
X, Y, Z = arrs
print("Got halo properties")

boxsize = 500 #Mpc/h
nthreads = 24
nbins = 15
bins = np.linspace(40.0, 150.0, nbins + 1) 

print("Running corrfunc")
xi_counts = xi(boxsize, nthreads, bins, X, Y, Z)
print("Ran corrfunc")

np.save('../results/xi{}.npy'.format(tag), np.array([bins, xi_counts]))
