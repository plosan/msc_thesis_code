load "Chains.m2"
load "../deformation/Deformation.m2"

aMax = 10;  -- Max exponent of x^a
bMax = 10;  -- Max exponent of x^b
pMax = 100; -- Upper bound for the characteristic; yes, I know 100 is not prime :)

for a from 3 to 3 do (
    for b from 7 to 7 do (
        -- Compute the monomials that give a constant Milnor number deformation
        -- of x^a + y^b. If there is no such monomial, skip to the next polynomial
        -- x^a + y^b. If there are such monomials, retain only the first in 
        -- lexicographic order in the exponents.
        mon := getDeformationMonomials(a, b);   -- Monomials of deformation
        if #mon == 0 then (
            continue;
        );
        c = (mon#0)#0;  -- Exponent of x in the monomial
        d = (mon#0)#1;  -- Exponent of y in the monomial

        -- Filenames for output
        polyName := concatenate("x", toString(a), "_+_y", toString(b), "_+_x", toString(c), "y", toString(d));
        file := concatenate("../out/deformation_e_chain/", polyName, ".txt");
        fileLevel := concatenate("../out/deformation_e_chain/", polyName, "_level.txt");

        for p from 2 to 100 do (
            -- Skip p's that are not prime
            if not isPrime(p) then (
                continue;
            );
            print(polyName);
            -- Computations
            R := GF(p)[x, y];               -- Polynomial ring Fp[x,y]
            g := x^a + y^b + x^c * y^d;     -- Deformation of x^a + y^b
            print(concatenate("p = ", toString(p)));
            out := eChainVerbose(g, 1);
            -- Print to file 
            file << "p = " << toString(p);
            file << ", level = " << toString(out_0) << endl;
            for i from 0 to (length out_1 - 1) do (
                file << "e = " << toString(i + 1) << " : " << toString(out_1#i) << endl;
            );
            file << endl;
            -- Print to fileLevel
            fileLevel << "p = " << toString(p);
            fileLevel << ", level = " << toString(out_0) << endl;
            print("");
        );

        file << close;
        fileLevel << close;
    );
);