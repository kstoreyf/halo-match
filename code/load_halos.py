import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from AbacusCosmos import Halos


halo_dir = '/mount/sirocco1/ksf293/halo_files_z0'
cat = Halos.make_catalog_from_dir(dirname=halo_dir, halo_type='Rockstar',
      load_subsamples=False, load_pids=False)
halos = cat.halos
print len(halos)
print (halos['parent_id'] != -1).mean()
halo0 = halos[0]
for field in sorted(halo0.dtype.fields):
  print(field, ':', halo0[field])

print 'Get mvirs'
hprop = 'vmax'
ms = [h[hprop] for h in halos]
print len(ms)
print min(ms), max(ms)
bins = np.logspace(np.log10(min(ms)),np.log10(max(ms)), 50)
n, bins, patches = plt.hist(ms, bins=bins, histtype='step', label='all halos')

subs = halos[halos['parent_id'] != -1]
hosts = halos[halos['parent_id'] == -1]
n, bins, patches = plt.hist(hosts[hprop], bins=bins, histtype='step', label='hosts')
n, bins, patches = plt.hist(subs[hprop], bins=bins, histtype='step', label='subhalos')
plt.xscale('log')
plt.yscale('log')
plt.ylim(10**0, 10**7)
#plt.xlabel(r'$M_{\mathrm{vir,halo}}$')
plt.xlabel(r'$v_{\mathrm{max}}$')
plt.ylabel(r'count')
plt.legend()
#bin_edges, bin_centers, hist = Halos.halo_mass_hist(cat.halos[0]['N'])
#plt.loglog(bin_centers, hist)
plt.savefig('../plots/vmax_func_subshosts.png')
