import numpy as np
from Corrfunc.theory.xi import xi
from Corrfunc.theory.wp import wp

import utils


tag = '_abacus_mstellar_'
mode = 'wp'
halos, arrs = utils.load_halos(tag, cols=['x','y','z'])
X, Y, Z = arrs
print("Got halo properties")

#Load matched catalog
print("Loading matched catalog")
mstellar = np.loadtxt("../catalogs/catalog_mstellar_abacus.dat")
print(len(mstellar))

X = X[~np.isnan(mstellar)]
Y = Y[~np.isnan(mstellar)]
Z = Z[~np.isnan(mstellar)]
print(len(X))
if 'abacus' in tag:
    boxsize = 500 #Mpc/h
elif 'ds14b' in tag:
    boxsize = 1000 #Mpc/h
else:
    raise ValueError
nthreads = 24
nbins = 15
bins = np.logspace(np.log10(0.1), np.log10(10.0), nbins + 1) #log
#bins = np.linspace(0.1, 10.0, nbins + 1) #regular
#bins = np.linspace(40.0, 150.0, nbins + 1) #rbig


print("Running corrfunc")
if mode=='xi':
    res = xi(boxsize, nthreads, bins, X, Y, Z)
elif mode=='wp':
    pimax = 40.0
    res = wp(boxsize, pimax, nthreads, bins, X, Y, Z)
print("Ran corrfunc")

np.save('../results/{}{}.npy'.format(mode, tag), np.array([bins, res]))
