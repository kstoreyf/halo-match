import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from AbacusCosmos import Halos
from AbundanceMatching import *



#Load matched catalog
print("Loading matched catalog")
mstellar = np.loadtxt("catalog_mstellar.dat")
print mstellar

#Load halos 
halo_dir = '/mount/sirocco1/ksf293/halo_files_z0'
print("Loading halos from {}".format(halo_dir))
cat = Halos.make_catalog_from_dir(dirname=halo_dir, halo_type='Rockstar',
      load_subsamples=False, load_pids=False)
halos = cat.halos
print("Loaded {} halos".format(len(halos)))

nbins = 12
mstellar_notnan = mstellar[~np.isnan(mstellar)]
print len(mstellar), len(mstellar_notnan)
bins = np.logspace(np.log10(min(mstellar_notnan)), 
        np.log10(max(mstellar_notnan)), nbins+1)
bincenters = 10**(0.5*(np.log10(bins[:-1]) + np.log10(bins[1:])))
print bins
print bincenters

bin_idxs = np.digitize(mstellar, bins)
nsats = np.zeros(nbins)
ncentrals = np.zeros(nbins)
for i in range(len(mstellar)):
    bin_idx = bin_idxs[i]-1
    # if nan, returns nbins
    if bin_idx < nbins:
        if halos['parent_id'][i]==-1:
            ncentrals[bin_idx] += 1
        else:
            nsats[bin_idx] += 1

fsat = nsats/(ncentrals+nsats)

plt.figure()
plt.plot(bincenters, fsat, ls='None', marker='o', color='purple')
plt.xlabel(r'$M_{\mathrm{stellar}}$')
plt.ylabel(r'$f_{\mathrm{sat}}$')
plt.savefig('../plots/fsat_mstellar.png')

sats = mstellar[halos['parent_id'] != -1]
centrals = mstellar[halos['parent_id'] == -1]
print len(sats), len(sats[~np.isnan(sats)])
print len(centrals), len(centrals[~np.isnan(centrals)])

n, bins, patches = plt.hist(centrals, bins=bins, histtype='step', label='centrals')
n, bins, patches = plt.hist(sats, bins=bins, histtype='step', label='satellites')
n, bins, patches = plt.hist(mstellar, bins=bins, histtype='step', label='all')
#plt.xscale('log')
plt.yscale('log')
#plt.ylim(10**0, 10**7)
#plt.xlabel(r'$M_{\mathrm{vir,halo}}$')
plt.xlabel(r'$M_{\mathrm{stellar}}$')
plt.ylabel(r'count')
plt.legend()
#bin_edges, bin_centers, hist = Halos.halo_mass_hist(cat.halos[0]['N'])
#plt.loglog(bin_centers, hist)
plt.savefig('../plots/mstellars_satscentrals.png')

