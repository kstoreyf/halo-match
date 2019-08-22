import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from AbacusCosmos import Halos
from AbundanceMatching import *


plot_dir = '../plots/plots_2019-08-22'
#LF_SCATTER_MULT = 2.5
LF_SCATTER_MULT = 1
 
smf_label = r'$M_{\mathrm{stellar}}$'
halo_label = r'$v_{\mathrm{max}}$'
n_label = 'n'

smf = np.loadtxt("smf_sdss_z0.dat")
smf_logM = smf[:,0]
smf_n = smf[:,1]
#lf = np.loadtxt("lf_test.dat")
#smf_logM = lf[:,0]
#smf_n = 10**lf[:,1]
#ext_range = (-25, -17)
ext_range = (9.5, 12.4)
#ext_range = (None, None)

print smf_logM
print smf_n
af = AbundanceFunction(smf_logM, smf_n, ext_range=ext_range, faint_end_first=True)
print af._x
print len(af._x)

plt.figure()
scatter = 0.15
remainder = af.deconvolute(scatter, 20)
x, nd = af.get_number_density_table()
plt.plot(x, remainder/nd);
plt.savefig("../plots/deconv.png")

#Load halos 
halo_dir = '/mount/sirocco1/ksf293/halo_files_z0'
print("Loading halos from {}".format(halo_dir))
cat = Halos.make_catalog_from_dir(dirname=halo_dir, halo_type='Rockstar',
      load_subsamples=False, load_pids=False)
halos = cat.halos
print("Loaded {} halos".format(len(halos)))

print 'subfrac'
print (halos['parent_id'] != -1).mean()
# only subhalos
#halos = halos[halos['parent_id'] != -1]
vmaxs = halos['vmax']

#check abundance function
plt.figure()
plt.semilogy(smf_logM, smf_n, label='SMF SDSS z=0')
x = np.linspace(min(smf_logM), max(smf_logM), 101)
plt.semilogy(x, af(x), label='abundance function')
plt.legend()
plt.xlabel(smf_label)
plt.ylabel(n_label)
plt.savefig("../plots/abundance_function.png")

#get number densities of the halo catalog
box_size = 500 #Mpc/h #got from header file, http://nbody.rc.fas.harvard.edu/public/S2016/schneider_spline_rockstar_halos/z0.000/header
#box_size = 737.789582411096376 #Mpc
nd_halos = calc_number_densities(vmaxs, box_size)
print 'check outside bounds'
print len(nd_halos)
print len(nd_halos[nd_halos<max(smf_n)])
nbin = 200
bins = np.linspace(vmaxs.min(), vmaxs.max(), int(nbin)+1)
nd_halos_binned = calc_number_densities_in_bins(vmaxs, box_size, bins)
print
print "CHECK"
print nd_halos
print af._nd_log
print af._x
print

#downsample
#step = 1000
#nd_halos = nd_halos[::step]
#vmaxs = vmaxs[::step]
#print(len(vmaxs))

#halo function
plt.figure()
plt.loglog(vmaxs, nd_halos, ls='None', marker='.')
plt.xlabel(halo_label)
plt.ylabel(n_label)
plt.savefig("../plots/halo_function.png")


#interp function
plt.figure()
x, nd = af.get_number_density_table()
plt.semilogy(x, nd, ls='None', marker='.')
plt.xlabel(smf_label)
plt.ylabel(n_label)
plt.savefig("../plots/interp.png")

print len(nd_halos)
print max(nd_halos)
print min(nd_halos)
#do abundance matching with no scatter
catalog_sm = af.match(nd_halos)
catalog_sm_scatter = af.match(nd_halos, scatter)

f = open('catalog_mstellar.dat', 'w')
np.savetxt(f, catalog_sm)

print len(catalog_sm)
print max(catalog_sm)
print min(catalog_sm)
print catalog_sm
plt.figure()
plt.semilogx(vmaxs, catalog_sm, ls='None', marker='.')
plt.xlabel(halo_label)
plt.ylabel(smf_label)
plt.savefig("../plots/abundance_matching.png")

plt.figure()
plt.semilogx(vmaxs, catalog_sm_scatter, ls='None', marker='.', alpha=0.1)
plt.xlabel(halo_label)
plt.ylabel(smf_label)
plt.savefig("../plots/abundance_matching_scatter.png")

plt.figure()
plt.semilogy(catalog_sm, vmaxs, ls='None', marker='.')
plt.ylabel(halo_label)
plt.xlabel(smf_label)
plt.savefig("../plots/abundance_matching_inv.png")

catalog_sm_binned = af.match(nd_halos_binned)
plt.figure()
plt.semilogx(bins, catalog_sm_binned, ls='None', marker='.')
plt.xlabel(halo_label)
plt.ylabel(smf_label)
plt.savefig("../plots/abundance_matching_binned.png")

#do abundance matching with some scatter
# don't think i need to multiply scatter by LF_SCATTER_MULT bc smf not lf??
#catalog_sc = af.match(nd_halos, scatter)

catalog_sm_notnan = catalog_sm[~np.isnan(catalog_sm)]
plt.figure()
plt.hist(catalog_sm_notnan, bins=50, histtype='step')
plt.xlabel(smf_label+' matched')
plt.ylabel('count')
plt.yscale('log')
plt.savefig("../plots/sm_catalog_matched.png")