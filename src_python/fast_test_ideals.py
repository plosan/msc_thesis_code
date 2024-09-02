
from matplotlib import pyplot as plt

import tools



if __name__ == "__main__":

    a = 7
    b = 5

    line_params = (b, a, a * b)

    points = [(u, v) for u in range(a + 1) for v in range(b + 1) if tools.line_func(line_params, (u, v)) <= 0]
    points_x = [point[0] for point in points]
    points_y = [point[1] for point in points]
    
    fig, ax = plt.subplots()
    ax.axvline(x=0)
    ax.axhline(y=0)
    ax.scatter(points_x, points_y, color='k')
    tools.plot_binomial_line(ax, b, a, a * b, color='b')
    tools.plot_binomial_line(ax, b, a, a * b - a - b, color='r')

    ax.set_aspect('equal')
    plt.show()
