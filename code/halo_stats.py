import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

import utils

plot_dir = '../plots/plots_2019-08-29'
tag = '_ds14b_log'

halo_label = r'$v_{\mathrm{max}}$'
n_label = 'n'

cols = ['vmax', 'parent_id']
halos, arrs = utils.load_halos(tag, cols)
vmaxs, parent_ids = arrs

subs = vmaxs[parent_ids != -1]
hosts = vmaxs[parent_ids == -1]

if 'log' in tag:
    bins = np.logspace(np.log10(min(vmaxs)),np.log10(max(vmaxs)), 50)
else:
    bins = 50
n, bins, patches = plt.hist(vmaxs, bins=bins, histtype='step', label='all')
n_s, bins_s, _ = plt.hist(subs, bins=bins, histtype='step', label='subhalos')
n_h, bins_s, _ = plt.hist(hosts, bins=bins, histtype='step', label='hosts')

plt.xlabel(halo_label)
plt.ylabel(n_label)
plt.yscale('log')
plt.legend()
plt.savefig("{}/hist_vmax{}.png".format(plot_dir, tag))

np.save('../results/hist_vmax{}.npy'.format(tag), np.array([bins, n, n_s, n_h]))

if 'log' in tag:
    bins = np.logspace(np.log10(min(vmaxs)),np.log10(max(vmaxs)), 15)
else:
    bins = 15
n_s, bins_s, _ = plt.hist(subs, bins=bins, histtype='step', label='subhalos')
n_h, bins_h, _ = plt.hist(hosts, bins=bins, histtype='step', label='hosts')
f_sub = n_s/n_h

np.save('../results/fsub_vmax{}.npy'.format(tag), np.array([bins, f_sub]))
