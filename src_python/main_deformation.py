import sys
from sage.all import *

import frobenius
import utils

def compute_kashiwara_number_v1(p, f):
    
    power_f = f ** (p - 1)
    froot_prev = frobenius.frobenius_root(p, 1, power_f)
    
    for e in range(2, 10):
        try:
            print('e = %2d. Computing power of the deformation...' %e)
            power_f = f ** (p ** e - 1)
        except OverflowError as error:
            print(f"{type(error).__name__} : {error}. Script will abort")
            sys.exit(1)
        else:
            print('e = %2d. Computing Frobenius root...' %e)
            froot = frobenius.frobenius_root(p, e, power_f) 
            if froot != froot_prev:
                print('e = %2d. Found!' %e)
                return e - 1
            froot_prev = froot
            

def compute_kashiwara_number_v2(p, f):
    
    f_p1 = f**(p - 1)   # f^(p - 1)
    power_f = f_p1      # Powers of f of the form f^(p^e - 1)
    froot_prev = R.ideal(1)                               # Previous Frobenius root to compare to
    
    froot = frobenius.frobenius_root(p, 1, power_f)
    if froot != froot_prev:
        print('e = %2d. Found!' %(1))
        return 1
    froot_prev = froot
    
    for e in range(2, 10):
        try:
            print('e = %2d. Computing power of the deformation...' %e)
            power_f = f ** (p ** e - 1)
        except OverflowError as error:
            print(f"{type(error).__name__} : {error}. Script will abort")
            sys.exit(1)
        else:
            print('e = %2d. Computing Frobenius root...' %e)
            froot = frobenius.frobenius_root(p, e, power_f) 
            if froot != froot_prev:
                print('e = %2d. Found!' %e)
                return e - 1
            froot_prev = froot

if __name__ == "__main__":
    # Setup
    p = 7
    e = 1
    R = PolynomialRing(GF(p), 'X, Y')
    gens = R.gens()
    X, Y = gens

    # Polynomial and deformation
    f = X**9 + Y**2
    
    
    
    # f0 = X**7 + Y**5
    # f = utils.deformation(f0, t33 = 1, t52 = 0, t43 = 0, t53 = 0)
    # f = utils.deformation(f0, t33 = 0, t52 = 1, t43 = 1, t53 = 0)
    
    # print(type(expression))
    
    for e in range(1, 5):
        power = p ** e - 1
        f_power = f ** power
        print(e, frobenius.frobenius_root(p, e, f_power).groebner_basis())
    
    
    
    
    # f = utils.deformation(f0, t33 = 0, t52 = 0, t43 = 0, t53 = 0)

    # Compute Frobenius roots

    
    
    
    # f_power = f ** (p - 1)
    
    # expression = frobenius._monomialize_polynomial(p**e, f_power, gens)
    
    # print('%15s%15s' %('Coeff', 'Basis Elem'))
    # for elem in expression:
    #     basis_elem = elem
    #     coeff = expression[basis_elem]
    #     coeff = coeff[0]
    #     mon1 = frobenius._exponents_to_monomial(basis_elem, gens)
    #     print('%15s%15s' %(str(coeff), str(mon1)))