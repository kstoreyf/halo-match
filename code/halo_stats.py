import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from halotools.sim_manager import CachedHaloCatalog



plot_dir = '../plots/plots_2019-08-27'
#tag = '_tiny'
tag = '_ds14b'

halo_label = r'$v_{\mathrm{max}}$'
n_label = 'n'

simname = 'ds14b'
#version_name = 'rockstar1{}'.format(tag)
version_name = 'rockstar1'
print("Loading halos from {}".format(simname))
halos = CachedHaloCatalog(simname=simname, halo_finder='rockstar', version_name=version_name, redshift=0.0)

print("Loaded {} halos".format(len(halos.halo_table['halo_id'])))

vmaxs = halos.halo_table['halo_vmax']

n, bins, patches = plt.hist(vmaxs, bins=50, histtype='step')
plt.xlabel(halo_label)
plt.ylabel(n_label)
plt.yscale('log')
plt.savefig("{}/hist_vmax{}.png".format(plot_dir, tag))

np.save('../results/hist_vmax{}.npy'.format(tag), np.array([bins, n]))
