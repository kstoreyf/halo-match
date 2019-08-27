import numpy as np

from halotools.sim_manager import RockstarHlistReader


sim_fn = '/nfs/slac/des/fs1/g/sims/yymao/ds14_b_sub'
input_fname = '{}/hlists/hlist_1.00000.list'.format(sim_fn)
#input_fname = '../data/hlist_1.00000_tiny.list'.format(sim_fn)
#tag = '_tiny'
tag = ''

columns_to_keep_dict = {'halo_id': (1, 'i8'), 'halo_parent_id': (5, 'i8'), 'halo_upid': (6, 'i8'), 'halo_vmax': (16, 'f4'), 'halo_x': (17, 'f4'), 'halo_y': (18, 'f4'), 'halo_z': (19, 'f4'), 'halo_mvir': (10, 'f4')}
#columns_to_keep_dict = {'halo_id': (1, np.dtype('i8')), 'halo_vmax': (16, np.dtype('f4')), 'halo_x': (17, np.dtype('f4')), 'halo_y': (18, np.dtype('f4')), 'halo_z': (19, np.dtype('f4')), 'halo_upid': (6, np.dtype('i8'))}
simname = 'ds14b'
halo_finder = 'rockstar'
redshift = 0.0
version_name = 'rockstar1'+tag
#output_fname = "/usr/tmp/halos_{}_{}.hdf5".format(simname, version_name)
output_fname = "../catalogs/halos_{}_{}.hdf5".format(simname, version_name)
Lbox = '1000.0' #Mpc/h
particle_mass = 5.6749434 #THIS IS FROM A FOUND HERE, CHANGE http://darksky.slac.stanford.edu/data_release/README.html
print("Loading halos from {}".format(simname))
reader = RockstarHlistReader(input_fname, columns_to_keep_dict, output_fname, simname, halo_finder, redshift, version_name, Lbox, particle_mass, overwrite=True)
columns_to_convert_from_kpc_to_mpc = []
reader.read_halocat(columns_to_convert_from_kpc_to_mpc, write_to_disk = True, update_cache_log = True) 
