loadPackage "TestIdeals"

p = 7
R = GF(p)[x, y]

g = y^2 - x^3
f = g^5 - x^5 * y^10
f = y^2 - x^3

e = 1
emax = 10

nuInv = {}
fRoots = {aux_froot}

-- Printing
-- print(concatenate("f = ", toString(f)))
print(concatenate("p = ", toString(p)))
print(concatenate("e = ", toString(e)))
-- print(concatenate("f = (y^2 - x^3)^5 - x^3 y^10"))
print(concatenate("f = y^2 - x^3"))
print("")

for e from 1 to emax do (
    exponent = p^e - 1;
    fRoot = frobeniusRoot(e, ideal(f^exponent));
    fRoots = append(fRoots, fRoot);
    print(concatenate("e = ", toString(e), "\tExponent = ", toString(exponent), "\tIdeal : ", toString(fRoot)))
);
