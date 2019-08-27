import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np


def main():

    plot_dir = '../plots/plots_2019-08-27'
    savetag = '_abacus_ds14b'
    save_fn = '{}/fsat_mstellar{}.png'.format(plot_dir, savetag)

    tags = ['_abacus', '_ds14b']
    labels = ['Abacus', 'ds14b']
    #tags = ['_ds14b']
    #labels = ['ds14b']
    ms = []
    fs = []
    for tag in tags:
        fsat_fn = '../results/fsat{}.npy'.format(tag)
        m, f = np.load(fsat_fn)
        ms.append(m)
        fs.append(f)

    plot_fsat(ms, fs, labels, save_fn)


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


if __name__=='__main__':
    main()
