loadPackage "TestIdeals"

p = 11
R = GF(p)[x, y]

g = y^2 - x^3
h = x^5 * y
f = g^2 - h

e = 1
emax = 5

nuInv = {}
fRoots = {aux_froot}

print(concatenate("p = ", toString(p)))
for e from 1 to emax do (
    exponent = p^e - 1;
    fRoot = frobeniusRoot(e, ideal(f^exponent));
    fRoots = append(fRoots, fRoot);
    print(concatenate("e = ", toString(e), "\tExponent = ", toString(exponent), "\tIdeal : ", toString(fRoot)))
);




