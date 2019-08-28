import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

import utils

plot_dir = '../plots/plots_2019-08-28'
#tag = '_tiny'
#tag = '_ds14b'
tag = '_abacus_subs'

halo_label = r'$v_{\mathrm{max}}$'
n_label = 'n'

cols = ['vmax', 'parent_id']
halos, arrs = utils.load_halos(tag, cols)
vmaxs, parent_ids = arrs

subs = vmaxs[parent_ids != -1]
hosts = vmaxs[parent_ids == -1]

n, bins, patches = plt.hist(vmaxs, bins=50, histtype='step', label='all')
ns, bins, patches = plt.hist(subs, bins=bins, histtype='step', label='subhalos')
nh, bins, patches = plt.hist(hosts, bins=bins, histtype='step', label='hosts')

plt.xlabel(halo_label)
plt.ylabel(n_label)
plt.yscale('log')
plt.legend()
plt.savefig("{}/hist_vmax{}.png".format(plot_dir, tag))

np.save('../results/hist_vmax{}.npy'.format(tag), np.array([bins, n, ns, nh]))
