import numpy as np
from Corrfunc.theory.xi import xi
from Corrfunc.theory.wp import wp

import AbundanceMatching as am

import utils


tag = '_abacus'
nthresh_str = '1e-4'
savetag = tag+'_n{}'.format(nthresh_str)
mode = 'wp'
halos, arrs = utils.load_halos(tag, cols=['x','y','z', 'vmax'])
X, Y, Z, vmaxs = arrs
print("Got halo properties")

#Load matched catalog
if 'mstellar' in savetag:
    print("Loading matched catalog")
    mstellar = np.loadtxt("../catalogs/catalog_mstellar{}.dat".format(tag))
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

if '_n' in savetag:
    nd_halos = am.calc_number_densities(vmaxs, boxsize)
    nthresh = float(nthresh_str)
    X = X[nd_halos<nthresh] #less than bc bigger halos have lower number dens
    Y = Y[nd_halos<nthresh]
    Z = Z[nd_halos<nthresh]
    print(len(X))

nthreads = 24
nbins = 15
bins = np.logspace(np.log10(0.01), np.log10(10.0), nbins + 1) #log
print(bins)
#bins = np.linspace(0.1, 10.0, nbins + 1) #regular
#bins = np.linspace(40.0, 150.0, nbins + 1) #rbig


print("Running corrfunc")
if mode=='xi':
    res = xi(boxsize, nthreads, bins, X, Y, Z)
elif mode=='wp':
    pimax = 40.0
    res = wp(boxsize, pimax, nthreads, bins, X, Y, Z)
print("Ran corrfunc")

np.save('../results/{}{}.npy'.format(mode, savetag), np.array([bins, res]))
