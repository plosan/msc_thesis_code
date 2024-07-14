load "Chains.m2"
load "../deformation/Deformation.m2"

aMax = 10;  -- Max exponent of x^a
bMax = 10;  -- Max exponent of x^b
pMax = 100; -- Upper bound for the characteristic; yes, I know 100 is not prime :)

for a from 3 to aMax do (
    for b from 7 to bMax do (
        -- Compute the monomials that give a constant Milnor number deformation
        -- of x^a + y^b. If there is no such monomial, skip to the next polynomial
        -- x^a + y^b. If there are such monomials, retain only the first in 
        -- lexicographic order in the exponents.
        defMon := getDeformationMonomials(a, b);   -- Monomials of deformation
        if #defMon == 0 then (
            continue;
        );

        for mon in defMon do (

            c := (mon)#0;  -- Exponent of x in the monomial
            d := (mon)#1;  -- Exponent of y in the monomial

            -- Filenames for output
            polyName := concatenate("x", toString(a), "_+_y", toString(b), "_+_x", toString(c), "y", toString(d));
            file := concatenate("../out/deformation_e_chain/", polyName, ".txt");
            fileLevel := concatenate("../out/deformation_e_chain/", polyName, "_level.txt");
            print(polyName);

            -- Optimizations for the max level of the Frobenius root
            level2 := 10;   -- Level of the singularity found two iterations ago
            level1 := 10;   -- Level of the singularity found an iteration ago
            emax := 10;     -- Max level of the Frobenius root computed
            consecSingL1 := false;  -- Set to true when two consecutive level 1 singularities are found
            optimizationFlag := false;  -- 
        
            for p from 2 to 100 do (
                -- Skip p's that are not prime
                if not isPrime(p) then (
                    continue;
                );
                -- Computations
                R := GF(p)[x, y];               -- Polynomial ring Fp[x,y]
                g := x^a + y^b + x^c * y^d;     -- Deformation of x^a + y^b
                print(concatenate("p = ", toString(p)));
                -- Compute
                if p >= 17 then (
                    emax = 1;
                    optimizationFlag = true;
                );
                print(concatenate("Computing for p = ", toString(p), ", e = ", toString(emax)));
                out := eChainVerbose(g, emax);
                -- Optimizations for the max level of the Frobenius root for the 
                -- nex iteration.
                levelMod := max(out_0, 1);
                level2 = level1;
                level1 = levelMod;
                emax = max(level1, level2);
                -- Print to file 
                file << "p = " << toString(p);
                file << ", level = " << toString(levelMod);
                if optimizationFlag then (
                    file << "*";
                );
                file << endl;
                for i from 0 to (length out_1 - 1) do (
                    file << "e = " << toString(i + 1) << " : " << toString(out_1#i) << endl;
                );
                file << endl;
                -- Print to fileLevel
                fileLevel << "p = " << toString(p);
                fileLevel << ", level = " << toString(levelMod);
                if optimizationFlag then (
                    fileLevel << "*";
                );
                fileLevel << endl;
                print("");
            );

            file << close;
            fileLevel << close;

        );
    );
);