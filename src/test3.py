from sage.all import *

import frobenius

def _exponents_to_monomial(exponents, gens):
    f = 1
    for i in range(len(gens)):
        f *= gens[i] ** exponents[i]
    return f

p = 11
e = 1
pe = p**e
R = PolynomialRing(GF(p), 'X, Y')
gens = R.gens()

X, Y = gens

f = X**7 + Y**5
f = f ** 10

f_coef = f.coefficients()
f_exps = f.exponents()

# print(f)

coef_tuple_list = []
base_tuple_list = []

print('%10s%10s%10s%10s' %('f coeff', 'f exps', 'coeff', 'basis'))
for i in range(len(f_coef)):
    coef_tuple = tuple([exp // pe for exp in f_exps[i]])
    base_tuple = tuple([exp % pe for exp in f_exps[i]])
    coef_tuple_list.append(coef_tuple)
    base_tuple_list.append(base_tuple)
    print('%10d%10s%10s%10s' %(f_coef[i], str(f_exps[i]), str(coef_tuple), str(base_tuple)))
    
# base_expression = dict()
# for i in range(len(f_coef)):
#     # Build monomial
#     coef = f_coef[i]
#     for j in range(len(gens)):
#         coef *= gens[j] ** coef_tuple_list[i][j]
#     print('%5d%10s%10s%10s%5s%s' %(f_coef[i], str(f_exps[i]), str(coef_tuple_list[i]), str(base_tuple_list[i]), '', str(coef)))
#     test = f_coef[i] * _exponents_to_monomial(coef_tuple_list[i], gens)
#     assert test == coef, f"Error {i}"
    
    
# for i in range(len(f_coef)):
#     for j in range(len(gens)):
#         assert f_exps[i][j] == pe * coef_tuple_list[i][j] + base_tuple_list[i][j], f"Error {i}, {j}"
froot = frobenius.frobenius_root(p, e, f)
pd = froot.primary_decomposition()

a = R.ideal(3 * X * Y, X**2, Y**2)
print(a.primary_decomposition())

a = R.ideal(X * Y)
for b in a.primary_decomposition():
    print(f'\t{b}')
    

    
# print(a.primary_decomposition())


# print(froot)
# print(pd)

# print(froot.gens())