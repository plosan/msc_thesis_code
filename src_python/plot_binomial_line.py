import numpy as np
from matplotlib import pyplot as plt

def line_func(a, b, x):
    return ((a * b) - b * x) / a

if __name__ == "__main__":

    a, b = 7, 4
    npoint = int(1e3)

    # Line b x + a y = a b
    u_axis = np.linspace(start=0, stop=a, num=npoint)
    v_axis = line_func(a, b, u_axis)

    # Integer points b x + a y <= a b
    int_points = []
    bd_int_points = []
    for u in range(a + 1):
        v_lim = int(np.floor(line_func(a, b, u)))
        int_points.extend([(u, v) for v in range(v_lim + 1)])
        bd_int_points.append(int_points[-1])
    u_int_points = [point[0] for point in int_points]
    v_int_points = [point[1] for point in int_points]

    # Remove boundary integer points with repeated y-coordinate
    indices = []
    for i in range(1, len(bd_int_points)):
        prev_y = bd_int_points[i-1][1]
        curr_y = bd_int_points[i][1]
        if curr_y == prev_y:
            indices.append(i)
        

    fig, ax = plt.subplots(figsize=(10,6))
    ax.set_title(f'f = x^{a} + y^{b}')
    ax.plot(u_axis, v_axis, color='b', lw=1)
    ax.scatter(u_int_points, v_int_points, color='r', edgecolor='r', lw=1)
    ax.set_xlim(-0.5, a + 1)
    ax.set_ylim(-0.5, b + 1)
    ax.set_aspect(1)
    ax.axvline(x=0, color='k', lw=0.5)
    ax.axhline(y=0, color='k', lw=0.5)
    plt.show()
