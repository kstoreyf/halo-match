import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np


def main():

    plot_dir = '../plots/plots_2019-08-27'
    savetag = '_abacus_ds14b'
    savefsat_fn = '{}/fsat_mstellar{}.png'.format(plot_dir, savetag)
    savehist_fn = '{}/hist_vmax{}.png'.format(plot_dir, savetag)    
    savexi_fn = '{}/xi{}.png'.format(plot_dir, savetag)
    
    tags = ['_abacus', '_ds14b']
    labels = ['Abacus', 'ds14b']
    #tags = ['_ds14b']
    #labels = ['ds14b']
    #tags = ['_abacus']
    #labels = ['Abacus']
    ms = []
    fs = []
    for tag in tags:
        fsat_fn = '../results/fsat{}.npy'.format(tag)
        m, f = np.load(fsat_fn)
        ms.append(m)
        fs.append(f)

    bins = []
    ns = []
    for tag in tags:
        hist_fn = '../results/hist_vmax{}.npy'.format(tag)
        b, n = np.load(hist_fn)
        bins.append(b)
        ns.append(n)

    rbins = []
    xis = []
    for tag in tags:
        xi_fn = '../results/xi{}.npy'.format(tag)
        rb, res = np.load(xi_fn)
        rbins.append(rb)
        xi = [r[3] for r in res]
        xis.append(xi)
    
    #plot_fsat(ms, fs, labels, savefsat_fn)
    #plot_hist(bins, ns, labels, savehist_fn)
    plot_xi(rbins, xis, labels, savexi_fn)

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


def plot_xi(bins, xis, labels, save_fn):
    markers = ['o', 'v']
    if type(bins[0]) is float:
        bins = [bins]
        xis = [xis]

    plt.figure()
    for i in range(len(bins)):
        b = bins[i]
        b_cent = 0.5*(b[:-1]+b[1:])
        xi = xis[i]
        print(b_cent)
        print(xi)
        plt.scatter(b_cent, xi, label=labels[i], marker=markers[i])

    #plt.yscale('log')
    plt.xlabel(r'$r$ (Mpc/h)')
    plt.ylabel(r'$\xi(r)$')
    plt.legend()

    plt.savefig(save_fn)


if __name__=='__main__':
    main()
