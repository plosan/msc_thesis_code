loadPackage "TestIdeals"

p = 11
e = 1
R = GF(p)[x, y]

g = y^2 - x^3
f = g^5 - x^5 * y^10
f = y^2 - x^3

pe = p^e
rmax = pe

nuInv = {}
auxRoot = frobeniusRoot(1, ideal(f))
fRoots = {auxRoot}
fpower = 1

-- Printing
-- print(concatenate("f = ", toString(f)))
print(concatenate("p = ", toString(p)))
print(concatenate("e = ", toString(e)))
-- print(concatenate("f = (y^2 - x^3)^5 - x^3 y^10"))
print(concatenate("f = y^2 - x^3"))
print("")
rprev = 1

for r from 1 to rmax do (
    fpower = f * fpower;
    fRoot = frobeniusRoot(e, ideal(fpower));
    if isSubset(auxRoot, fRoot) == false then ( -- nu-invariant found
        -- Printing
        print(concatenate("[", toString(rprev), ", ", toString(r - 1), "]: ", toString(auxRoot)));
        rprev = r;
        -- Computations
        nuInv = append(nuInv, r - 1);
        auxRoot = fRoot;
        fRoots = append(fRoots, fRoot);
    );
);

-- Printing
print("");
print(concatenate("Nu-invariants (<= ", toString(rmax), "): ", toString(nuInv)))

-- rprev = 1
-- for i from 0 to (length(nuInv) - 1) do (
--     print("");
--     print(concatenate("In [", toString(rprev), ", ", toString(nuInv#i), "]: ", toString(fRoots#i)));
--     rprev = nuInv#i + 1;
-- )
