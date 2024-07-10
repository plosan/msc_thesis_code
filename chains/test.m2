load "Monomialize.m2"
load "NewFrobeniusRoots.m2"
loadPackage "TestIdeals"

p = 11
R = GF(p)[x_1, x_2]



g = x_2^2 - x_1^3
h = x_1^5 * x_2
f = g^2 - h

e = 1
emax = 5

N = 2

nuInv = {}
fRoots = {aux_froot}

print(concatenate("p = ", toString(p)))
for e from 1 to emax do (
    pe = p^e;
    exponent = pe - 1;
    I = ideal(f^exponent);
    fRoot = newFrobeniusRoot(e, I);
    fRoots = append(fRoots, fRoot);
    print(concatenate("e = ", toString(e), "\tExponent = ", toString(exponent), "\tIdeal : ", toString(fRoot)));
);

