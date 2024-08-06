-- Write script docstring
load "Chains.m2"

aMax = 15;  -- Max exponent of x^a
bMax = 15;  -- Max exponent of x^b
pMax = 200; -- Upper bound for the characteristic; yes, I know 100 is not prime :)

for a from 2 to aMax do (
    for b from 2 to bMax do (
        -- Filenames for output
        ab := a * b;
        polyName := concatenate("x", toString(a), "_+_y", toString(b));
        file := concatenate("../data/binomial_r_chain_2/", polyName, ".txt");
        file << "" << endl;
        -- fileNuInv := concatenate("../out/binomial_r_chain_nu_invariants/", polyName, "_nu_invariants.txt");
        -- Compute for primes
        for p from 2 to pMax do (
            if not isPrime(p) then (
                continue;
            );
            -- Skip primes that are not congruent to +1 or -1 mod a*b
            if not ((p % ab == 1) or (p % ab == ab - 1)) then (
                continue;
            );
            -- Setup
            R := GF(p)[x, y];
            f := x^a + y^b;
            isIrred := isPrime(ideal(f));
            e := 1;
            -- Print
            print(concatenate("f = ", polyName));
            print(concatenate("p = ", toString(p), ", e = ", toString(e)));
            print(concatenate("irred = ", toString(isIrred)));
            -- Computations
            out := rChainVerbose(f, e);
            nuInv := out_0;
            fRoots := out_1;
            
            -- Print to file
            fileAppend = openOutAppend(file);
            fileAppend << "p = " << toString(p) << endl;
            fileAppend << "irred = " << toString(isIrred) << endl;
            fileAppend << "nu-inv = " << toString(nuInv) << endl;
            rprev := 1;
            for i from 0 to (length nuInv - 1) do (
                fileAppend << "[" << toString(rprev) << ", " << toString(nuInv#i) << "] : " << toString(fRoots#i) << endl;
                rprev = nuInv#i + 1;
            );
            fileAppend << endl << close;

            -- -- Print to fileNuInv
            -- fileNuInv << "p = " << toString(p);
            -- fileNuInv << ", irred = ";
            -- if isIrred then (  -- Overengineered to print with same col width
            --     fileNuInv << "true ";
            -- ) else (
            --     fileNuInv << "false";
            -- );
            -- fileNuInv << ", nu-inv = " << toString(nuInv) << endl;
        );
        -- file << close;
        -- fileNuInv << close;
    );
);