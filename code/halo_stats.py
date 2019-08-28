import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np



plot_dir = '../plots/plots_2019-08-27'
#tag = '_tiny'
#tag = '_ds14b'
tag = '_abacus'

halo_label = r'$v_{\mathrm{max}}$'
n_label = 'n'

if 'abacus' in tag:
    from AbacusCosmos import Halos

    halo_dir = '/mount/sirocco1/ksf293/halo_files_z0'
    print("Loading halos from {}".format(halo_dir))
    cat = Halos.make_catalog_from_dir(dirname=halo_dir, halo_type='Rockstar',
          load_subsamples=False, load_pids=False)
    halos = cat.halos
    vmaxs = halos['vmax']
    print("Loaded {} halos".format(len(halos)))

elif 'ds14b' in tag:
    from halotools.sim_manager import CachedHaloCatalog
    
    simname = 'ds14b'
    #version_name = 'rockstar1{}'.format(tag)
    version_name = 'rockstar1'
    print("Loading halos from {}".format(simname))
    halos = CachedHaloCatalog(simname=simname, halo_finder='rockstar', version_name=version_name, redshift=0.0)
    vmaxs = halos.halo_table['halo_vmax']
    print("Loaded {} halos".format(len(halos.halo_table['halo_id'])))

else:
    raise ValueError("Tag '{}' not recognized".format(tag))


n, bins, patches = plt.hist(vmaxs, bins=50, histtype='step')
plt.xlabel(halo_label)
plt.ylabel(n_label)
plt.yscale('log')
plt.savefig("{}/hist_vmax{}.png".format(plot_dir, tag))

np.save('../results/hist_vmax{}.npy'.format(tag), np.array([bins, n]))
