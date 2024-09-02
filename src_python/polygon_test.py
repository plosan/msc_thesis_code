import tools
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":
    
    min_exp = 1
    max_exp = 20
    monomial_count = 50
    x_exps = np.random.randint(low=min_exp, high=max_exp, size=monomial_count).tolist()
    y_exps = np.random.randint(low=min_exp, high=max_exp, size=monomial_count).tolist()
    
    monomials = list(zip(x_exps, y_exps))
    
    vertices = tools.compute_min_gen_set(monomials)
    x_vertices = [monomial[0] for monomial in vertices]
    y_vertices = [monomial[1] for monomial in vertices]
    
    
    
    fig, ax = plt.subplots()
    ax.scatter(x_exps, y_exps, color='k')
    ax.plot(x_vertices, y_vertices, '-o', color='r')
    ax.plot([x_vertices[0], x_vertices[0]], [y_vertices[0], max_exp+100], '-o', color='r')
    ax.plot([x_vertices[-1], max_exp+100], [y_vertices[-1], y_vertices[-1]], '-o', color='r')
    # ax.axhline(y=y_vertices[-1], xmin=x_vertices[-1])
    ax.set_xlim(-0.5, max_exp + 1)
    ax.set_ylim(-0.5, max_exp + 1)
    ax.set_aspect(1)
    ax.axvline(x=0, color='k', lw=0.5)
    ax.axhline(y=0, color='k', lw=0.5)
    plt.show()
    