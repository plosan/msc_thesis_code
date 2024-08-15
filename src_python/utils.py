from sage.all import *

def deformation(f, t33 = 0, t52 = 0, t43 = 0, t53 = 0):
    X, Y = f.parent().gens()
    g = f - t33 * X**3 * Y**3 - t52 * X**5 * Y**2 - t43 * X**4 * Y**3 - t53 * X**5 * Y**3
    return g