import numpy as np



def load_halos(tag, cols, subsample=None):
    if 'abacus' in tag:
        from AbacusCosmos import Halos
    
        halo_dir = '/mount/sirocco1/ksf293/halo_files_z0'
        print("Loading halos from {}".format(halo_dir))
        cat = Halos.make_catalog_from_dir(dirname=halo_dir, halo_type='Rockstar',
              load_subsamples=False, load_pids=False)
        halos = cat.halos
        if subsample:
            halos = halos[:subsample]

        arrs = []
        for col in cols:
            poss = {'x':0, 'y':1,'z':2}
            if col in poss:
                arrs.append(halos['pos'][:,poss[col]])
            else:
                arrs.append(halos[col])
        print("Loaded {} halos".format(len(halos)))
    
    elif 'ds14b' in tag:
        from halotools.sim_manager import CachedHaloCatalog
    
        simname = 'ds14b'
        #version_name = 'rockstar1{}'.format(tag)
        version_name = 'rockstar1'
        print("Loading halos from {}".format(simname))
        halos = CachedHaloCatalog(simname=simname, halo_finder='rockstar', version_name=version_name, redshift=0.0)
        arrs = []
        for col in cols:
            arrs.append(halos.halo_table['halo_{}'.format(col)])
        print("Loaded {} halos".format(len(halos.halo_table['halo_id'])))
        
    else:
        raise ValueError("Tag '{}' not recognized".format(tag)) 

    return halos, arrs
