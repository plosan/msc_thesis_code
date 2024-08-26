from matplotlib import pyplot as plt

def line_func(line_params, point):
    a, b, c = line_params
    x, y = point
    return a * x + b * y - c


def monomials_of_deformation(a, b):

    line_params = (b, a, a * b)
    mon_def = [(i, j) for i in range(a-1) for j in range(b-1) \
               if line_func(line_params, (i,j)) > 0]
    return mon_def

def _binomial_line_func(a, b, c, x):
    return (c - a * x) / b

def plot_binomial_line(ax, a, b, c, **kwargs):
    """Plots the line a x + b y = c in the first quadrant. It is therefore assumed that a, b, c are
    strictly positive real numbers.
    Args:
        ax (matplotlib.axes._axes.Axes): axis where the line will be plotted.
        a (float): positive real number, coefficient of x in the line equation.
        b (float): positive real number, coefficient of y in the line equation.
        c (float): positive real number, independent term in the line equation.
        **kwargs (dict): ax.plot kwargs parameter.
    Returns:
        None
    Raises:
        ValueError: if either a, b or c are <= 0.
    """
    if not all([a > 0, b > 0, c > 0]):
        raise ValueError("Parameters a, b, c for line a x + b y = c must be > 0")
    x_coords = [0, c/a]
    y_coords = [c/b, 0]
    ax.plot(x_coords, y_coords, **kwargs)

import math

if __name__ == "__main__":

    a = 7
    b = 5

    p = 71
    print(p % (a*b))

    # quit()
    for u in range(1, 3*a):
            num = (u * p - 1) / a
            fnum = int(math.floor(num))
            cnum = int(u * (p - 1) // a)
            print(u, num, fnum, fnum - cnum)

    quit()

    monomials = [(i,j) for i in range(a) for j in range(b)]
    monomials_x = [mon[0] for mon in monomials]
    monomials_y = [mon[1] for mon in monomials]

    mon_def = monomials_of_deformation(a, b)
    mon_def_x = [mon[0] for mon in mon_def]
    mon_def_y = [mon[1] for mon in mon_def]

    fig, ax = plt.subplots()

    ax.scatter(monomials_x, monomials_y, c='k', facecolor='k')
    ax.scatter(mon_def_x, mon_def_y, c='b', facecolor='b', label="mu-constant def monomials")
    plot_binomial_line(ax, b, a, a * b, color='r', label='b x + a y = a b')
    ax.set_xlim(-0.5, a + 1)
    ax.set_ylim(-0.5, b + 1)
    ax.set_aspect(1)
    ax.axvline(x=0, color='k', lw=0.5)
    ax.axhline(y=0, color='k', lw=0.5)
    ax.legend()
    plt.show()