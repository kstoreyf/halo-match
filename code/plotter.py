import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np


def main():

    plot_dir = '../plots/plots_2019-08-28'
    savetag = '_abacus_ds14b_mstellar_log'
    savefsat_fn = '{}/fsat_mstellar{}.png'.format(plot_dir, savetag)
    savehist_fn = '{}/hist_vmax{}.png'.format(plot_dir, savetag)
    mode = 'wp'    
    savecf_fn = '{}/{}{}.png'.format(plot_dir, mode, savetag)
    
    restag = '_mstellar_log'
    tags = ['_abacus{}'.format(restag), '_ds14b{}'.format(restag)]
    labels = ['Abacus', 'ds14b']
    #tags = ['_ds14b']
    #labels = ['ds14b']
    #tags = ['_abacus_log']
    #labels = ['Abacus']
    
    #ms = []
    #fs = []
    #for tag in tags:
    #    fsat_fn = '../results/fsat{}.npy'.format(tag)
    #    m, f = np.load(fsat_fn)
    #    ms.append(m)
    #    fs.append(f)

    #bins = []
    #ns = []
    #for tag in tags:
    #    hist_fn = '../results/hist_vmax{}.npy'.format(tag)
    #    b, n = np.load(hist_fn)
    #    bins.append(b)
    #    ns.append(n)

    rbins = []
    cfs = []
    for tag in tags:
        cf_fn = '../results/{}{}.npy'.format(mode, tag)
        rb, res = np.load(cf_fn)
        print(res)
        rbins.append(rb)
        cf = [r[3] for r in res]
        cfs.append(cf)
    
    #plot_fsat(ms, fs, labels, savefsat_fn)
    #plot_hist(bins, ns, labels, savehist_fn)
    plot_cf(rbins, cfs, labels, savecf_fn)

def plot_fsat(ms, fs, labels, save_fn):
    markers = ['o', 'v']
    if type(ms[0]) is float:
        ms = [ms]
        fs = [fs]

    plt.figure()
    for i in range(len(ms)):
        m = ms[i]
        f = fs[i]
        plt.scatter(m, f, label=labels[i], marker=markers[i])
    
    plt.xlabel(r'$M_{\mathrm{stellar}}$')
    plt.ylabel(r'$f_{\mathrm{sat}}$')
    plt.legend()

    plt.savefig(save_fn)


def plot_hist(bins, ns, labels, save_fn):
    if type(bins[0]) is float:
        bins = [bins]
        ns = [ns]
    
    plt.figure()
    for i in range(len(bins)):
        b = bins[i]
        b_cent = 0.5*(b[:-1]+b[1:])
        n = ns[i]
        plt.step(b_cent, n, label=labels[i])

    plt.yscale('log')
    plt.xlabel(r'$v_{\mathrm{max}}$')
    plt.ylabel('n')
    plt.legend()

    plt.savefig(save_fn) 


def plot_cf(bins, cfs, labels, save_fn):
    markers = ['o', 'v']
    if type(bins[0]) is float:
        bins = [bins]
        cfs = [cfs]

    plt.figure()
    for i in range(len(bins)):
        b = bins[i]
        b_cent = 0.5*(b[:-1]+b[1:])
        cf = cfs[i]
        plt.scatter(b_cent, cf, label=labels[i], marker=markers[i])

    #plt.yscale('log')
    plt.xlabel(r'$r$ (Mpc/h)')
    if 'xi' in save_fn:
        plt.ylabel(r'$\xi(r)$')
    elif 'wp' in save_fn:
        plt.ylabel(r'$w_p(r_p)$')
    else:
        raise ValueError
    if 'log' in save_fn:
        plt.xscale('log')
        plt.yscale('log')
    
    plt.legend()

    plt.savefig(save_fn)


if __name__=='__main__':
    main()
