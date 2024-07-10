loadPackage "TestIdeals"

p = 11
e = 3
R = GF(p)[x, y]

g = y^2 - x^3
h = x^5 * y
f = g^2 - h

pe = p^e
rmax = pe

nuInv = {}
auxRoot = frobeniusRoot(1, ideal(f))
fRoots = {auxRoot}
fpower = 1

-- Printing
print(concatenate("f = ", toString(f)))
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




