import math
import numpy as np
import sys
from matplotlib import pyplot as plt

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

def last_frobenius_root_gens(a, b):

    c = a * b
    d = a * b - a - b

    gens = [(0, math.ceil(_binomial_line_func(b, a, d, 0)))]
    for i in range(1, math.ceil(d / b) + 1):
        print(f"i = {i}")
        j = math.ceil(_binomial_line_func(b, a, d, i))
        if j < gens[-1][1]:
            gens.append((i, j))
    return gens

def milnor_number(a, b):
    return (a - 1) * (b - 1)
        

if __name__ == "__main__":

    # x^4+y^7 + t_1*x^2*y^4+t_2*x^2*y^5
    a, b = 7, 5
    if len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        if a < b:
            a, b = b, a

    npoint = int(1e3)

    # Line b x + a y = a b
    u_axis = np.linspace(start=0, stop=a, num=npoint)
    v_axis = _binomial_line_func(b, a, a * b, u_axis)

    # Integer points b x + a y <= a b
    int_points = []
    bd_int_points = []
    for u in range(a + 1):
        v_lim = int(np.floor(_binomial_line_func(b, a, a * b, u)))
        int_points.extend([(u, v) for v in range(v_lim + 1)])
        bd_int_points.append(int_points[-1])
    u_int_points = [point[0] for point in int_points]
    v_int_points = [point[1] for point in int_points]

    with open('outfile.txt', 'w') as file:
        for point in int_points:
            file.write(f'\draw[pointstyle1] ({point[0]},{point[1]}) circle (2.5pt);\n')

    # Remove boundary integer points with repeated y-coordinate
    indices = []
    for i in range(1, len(bd_int_points)):
        prev_y = bd_int_points[i-1][1]
        curr_y = bd_int_points[i][1]
        if curr_y == prev_y:
            indices.append(i)
    
    print("Last frobenius root gens")
    print(last_frobenius_root_gens(a, b))
    print()

    fig, ax = plt.subplots(figsize=(10,6))
    ax.set_title(f'f = x^{a} + y^{b}, mu = {milnor_number(a, b)}')
    print(type(ax))
    plot_binomial_line(ax, b, a, a * b, color='r', label='b x + a y = a b')
    plot_binomial_line(ax, b, a, a * b - a - b, color='b', label='b x + a y = a b - a - b')
    plot_binomial_line(ax, b, a, a * b - a - b + 1, color='g', label='b x + a y = a b - a - b + 1')
    plot_binomial_line(ax, b, a, 15, color='m', label='b x + a y = 15')
    plot_binomial_line(ax, b, a, 16, color='y', label='b x + a y = 16')
    ax.scatter(u_int_points, v_int_points, color='r', edgecolor='r', lw=1)
    ax.set_xlim(-0.5, a + 1)
    ax.set_ylim(-0.5, b + 1)
    ax.set_aspect(1)
    ax.axvline(x=0, color='k', lw=0.5)
    ax.axhline(y=0, color='k', lw=0.5)
    ax.legend()
    plt.show()
