load "Chains.m2"
load "../deformation/Deformation.m2"

aMax = 10;  -- Max exponent of x^a
bMax = 10;  -- Max exponent of x^b
pMax = 100; -- Upper bound for the characteristic; yes, I know 100 is not prime :)

for a from 8 to aMax do (
    for b from a to bMax do (
        -- Compute the monomials that give a constant Milnor number deformation
        -- of x^a + y^b. If there is no such monomial, skip to the next polynomial
        -- x^a + y^b. If there are such monomials, retain only the first in 
        -- lexicographic order in the exponents.
        defMon := getDeformationMonomials(a, b);   -- Monomials of deformation
        if #defMon == 0 then (  -- No deformation, skip
            continue;
        );

        for mon in defMon do (
            c := (mon)#0;  -- Exponent of x in the monomial
            d := (mon)#1;  -- Exponent of y in the monomial
            -- Filenames for output
            polyName := concatenate("x", toString(a), "_+_y", toString(b), "_+_x", toString(c), "y", toString(d));
            file := concatenate("../out/deformation_r_chain/", polyName, ".txt");
            fileNuInv := concatenate("../out/deformation_r_chain_nu_invariant/", polyName, "_nu_invariants.txt");
            -- Computations
            e := 1;
        
            for p from 2 to 100 do (
            -- Skip not primes
                if not isPrime(p) then (
                    continue;
                );
                -- Setup
                R := GF(p)[x, y];               -- Polynomial ring Fp[x,y]
                g := x^a + y^b + x^c * y^d;     -- Deformation of x^a + y^b
                isIrred := isPrime(ideal(g));
                -- Print
                print(concatenate("f = ", polyName));
                print(concatenate("p = ", toString(p), ", e = ", toString(e)));
                print(concatenate("irred = ", toString(isIrred)));
                
                -- Computations
                out := rChainVerbose(g, e);
                nuInv := out_0;
                fRoots := out_1;

                -- Print to file
                file << "p = " << toString(p);
                file << ", irred = " << toString(isIrred) << endl;
                file << "nu-inv = " << toString(nuInv) << endl;
                rprev := 1;
                for i from 0 to (length nuInv - 1) do (
                    file << "[" << toString(rprev) << ", " << toString(nuInv#i) << "] : " << toString(fRoots#i) << endl;
                    rprev = nuInv#i + 1;
                );
                file << endl;

                -- Print to fileNuInv
                fileNuInv << "p = " << toString(p);
                fileNuInv << ", irred = ";
                if isIrred then (  -- Overengineered to print with same col width
                    fileNuInv << "true ";
                ) else (
                    fileNuInv << "false";
                );
                fileNuInv << ", nu-inv = " << toString(nuInv) << endl;
            );
            file << close;
            fileNuInv << close;
        );
    );
);