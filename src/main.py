import math
import numpy as np

from sage.all import *  
from matplotlib import pyplot as plt
    
import frobenius

OVERFLOW_LIM = 2**16 - 1

def fun1(val, sgn = 1):
    return sgn * np.power(val, 1.5)

def to_base_n(a, n):
    
    coefs = [a % n]
    while a > 0:
        a -= coefs[-1]
        a = int(a / n)
        coefs.append(a % n)
    return coefs

def check_base_n(a, n, coefs):

    b = 0
    power_n = 1
    for i in range(len(coefs)):
        b += coefs[i] * power_n
        power_n *= n
    
    return (a - b) == 0

def nice_base_n_expansion(a, n):
    coefs = to_base_n(a, n)
    parts = [f'{coefs[i]} * {n}^{i}' for i in range(len(coefs))]
    out = f"{a} = {' + '.join(parts)}"
    return out

def plot_nu_invariants(p, e, f, num_nu_inv = 10):

    nu_inv = frobenius.compute_nu_invariants(p, e, f, num_nu_inv)

    x_axis = [i + 1 for i in range(num_nu_inv)]
    fig, ax = plt.subplots()
    ax.plot(x_axis, nu_inv, marker = 'o')
    plt.show()

def compare_nu_invariants(p, e, polynomials, num_nu_inv = 10):

    nu_inv = [frobenius.compute_nu_invariants(p, e, f, num_nu_inv) for f in polynomials]
    max_nu_inv = max([elem[-1] for elem in nu_inv])

    x_axis = [i + 1 for i in range(num_nu_inv)]
    fig, ax = plt.subplots()
    [ax.plot(x_axis, nu_inv[i], marker = 'o', label = str(polynomials[i])) for i in range(len(polynomials))]
    ax.set_xlim([0, num_nu_inv + 1])
    ax.set_ylim([0, 10 * (math.ceil(max_nu_inv / 10) + 1)])
    ax.grid()
    ax.legend(loc = 'upper left')
    plt.show()

def deformation_f(f, t33, t52, t43, t53):
    X, Y = f.parent().gens()
    g = f - t33 * X**3 * Y**3 - t52 * X**5 * Y**2 - t43 * X**4 * Y**3 - t53 * X**5 * Y**3
    return g


if __name__ == "__main__":

    p = 71
    e = 1
    R = PolynomialRing(GF(p), 'X, Y')
    gens = R.gens()

    X, Y = gens

    # def_f = X**3 + Y**2 + X * Y

    f = X**7 + Y**5
    # g = X**5 + Y**7 + X**3 * Y**3

    # for e in range(1, 10):
    #     power = p ** e
    #     print(e, f**power)

    print(X**(2**16 - 1))

    print('Computing...')
    froot2 = frobenius.frobenius_root(p, 1, f**(p**1 - 1))

    print(froot2)


    quit()

    # g = X**2 + Y**7
    # h = X**2 + Y**4

    for elem in dir(f):
        print(elem)
    compare_nu_invariants(p, e, (f, g), num_nu_inv = 20)