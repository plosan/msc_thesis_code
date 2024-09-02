import math
from matplotlib import pyplot as plt

import tools



if __name__ == "__main__":

    a = 25
    b = 25

    def_mon = tools.mu_const_def_monomials(a, b)
    def_mon_x = [mon[0] for mon in def_mon]
    def_mon_y = [mon[1] for mon in def_mon]

    val_mon = tools.mu_const_def_monomials_values(a, b, def_mon)
    values_list = sorted(list(val_mon.keys()))
    
    for value in values_list:
        print("%10d%5s%s" %(value, "", val_mon[value])) 

    fig, ax = plt.subplots()
    tools.plot_binomial_line(ax, b, a, a * b, color='r', label="b x + a y = a b")
    ax.axvline(x=a-2, color="r", label="x = a - 1")
    ax.axhline(y=b-2, color="r", label="y = b - 1")
    ax.scatter(def_mon_x, def_mon_y, c='b', facecolor='b', label="mu-constant def monomials")
    ax.set_xlim(-0.5, a + 1)
    ax.set_ylim(-0.5, b + 1)
    ax.set_aspect(1)
    ax.axvline(x=0, color='k', lw=0.5)
    ax.axhline(y=0, color='k', lw=0.5)
    ax.legend()
    plt.show()