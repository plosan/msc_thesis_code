import copy
import numpy as np
from matplotlib import pyplot as plt

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

def milnor_number(a, b):
    return (a - 1) * (b - 1)

def point_line_distance(point, line):
    x, y = point
    a, b, c = line
    return np.abs(a * x + b * y + c) / np.sqrt(a**2 + b**2)

def convex_hull(points):

    point_list = copy.deepcopy(points)
    point_list.sort()

    convex_hull = [point_list[0]]
    for i in range(1, len(point_list)):
        x_prev = convex_hull[-1][0]
        y_prev = convex_hull[-1][1]
        x_curr = point_list[i][0]
        y_curr = point_list[i][1]
        if x_curr > x_prev and y_curr < y_prev:
            convex_hull.append(point_list[i])
    return convex_hull

if __name__ == "__main__":

    a = 7
    b = 5

    # Integer points b x + a y <= a b
    int_points = [(i,j) for i in range(a) for j in range(b) if b * i + a * j <= a * b]
    # bd_int_points = []
    # for u in range(a + 1):
    #     v_lim = int(np.floor(_binomial_line_func(b, a, a * b, u)))
    #     int_points.extend([(u, v) for v in range(v_lim + 1)])
    #     bd_int_points.append(int_points[-1])
    # u_int_points = [point[0] for point in int_points]
    # v_int_points = [point[1] for point in int_points]



    line = (b, a, 0)
    dist_int_points = [(point_line_distance(point, line), point) for point in int_points]
    dist_int_points.sort()
    int_points = [pair[1] for pair in dist_int_points]
    subset_int_points = [pair[1] for pair in dist_int_points if b * pair[1][0] + a * pair[1][1] <= a * b - a - b]
    x_integer_points = [point[0] for point in int_points]
    y_integer_points = [point[1] for point in int_points]




    for i in range(len(subset_int_points)):
        ch = convex_hull(int_points[i:])
        ch.sort()
        print('%10s : %s' %(str(subset_int_points[i]), str(ch)))

    # quit()
    fig, ax = plt.subplots(figsize=(10,6))
    ax.set_title(f'f = x^{a} + y^{b}, mu = {milnor_number(a, b)}')
    print(type(ax))
    plot_binomial_line(ax, b, a, a * b, color='r', label='b x + a y = a b')
    plot_binomial_line(ax, b, a, a * b - a - b, color='b', label='b x + a y = a b - a - b')
    plot_binomial_line(ax, b, a, a * b - a - b + 1, color='g', label='b x + a y = a b - a - b + 1')

    # for c in c_list:
    #     print(b, a, c)
    #     plot_binomial_line(ax, b, a, c, lw=0.5)
    ax.scatter(x_integer_points, y_integer_points, color='r', edgecolor='r', lw=1)
    ax.set_xlim(-0.5, a + 1)
    ax.set_ylim(-0.5, b + 1)
    ax.set_aspect(1)
    ax.axvline(x=0, color='k', lw=0.5)
    ax.axhline(y=0, color='k', lw=0.5)
    ax.legend()
    plt.show()