from sage.all import *
from sage.arith.power import generic_power

from sage.symbolic.ring import SymbolicRing as SR

R = SR()
X = R.var('X')
Y = R.var('Y')

print(X)
print(Y)

f = X**7 + Y**5
print(f)
print(f**2)
print(f**3)
print(f**4)



quit()
p = 71
R = PolynomialRing(GF(p), 'X, Y')
X, Y = R.gens()
f = X**7 + Y**5

for elem in dir(R):
    print(elem)


for e in range(1, 10):
    exponent = p**e - 1
    print(e, exponent, type(exponent))
    print(f**exponent)