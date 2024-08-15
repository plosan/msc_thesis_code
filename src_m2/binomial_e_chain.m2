-- binomial_e_chain.m2
-- For all primes 2 <= p <= pMax, this script does the following:
--      - Compute the level of the singularity of binomials f = x^a + y^b for
--        2 <= a <= aMax, 2 <= b <= bMax.
--      - Compute the ideals in the descending chain (f^(p^i - 1))^[1 / p^i], 
--        until stabilization.
--      - Print the process on the screen.
--      - Save to a file titled xa_+_yb.txt the following: p, level, ideals above.
--      - Save to a file titled xa_+_yb_level.txt the following: p, level.
load "Chains.m2"

aMax = 10;  -- Max exponent of x^a
bMax = 10;  -- Max exponent of x^b
pMax = 100; -- Upper bound for the characteristic; yes, I know 100 is not prime :)

for a from 2 to aMax do (
    for b from a to bMax do (
        -- Name of the polynomial for file naming purposes
        polyName := concatenate("x", toString(a), "_+_y", toString(b));
        file := concatenate("../out/binomial_e_chain/", polyName, ".txt");
        fileLevel := concatenate("../out/binomial_e_chain_level/", polyName, "_level.txt");
        print(polyName);
        -- Compute for primes
        for p from 2 to 100 do (
            if isPrime(p) then (
                print(concatenate("p = ", toString(p)));
                R := GF(p)[x, y];
                f := x^a + y^b;
                isIrred = isPrime(ideal(f));
                -- Printing and computing
                print(polyName);
                out := eChainVerbose(f, 10);

                -- Print to file
                file << "p = " << toString(p);
                if isIrred then (
                    file << ", irred = true ";
                ) else (
                    file << ", irred = false";
                );
                file << ", level = " << toString(out_0) << endl;
                for i from 0 to (length out_1 - 1) do (
                    file << "e = " << toString(i + 1) << ", " << toString(out_1#i) << endl;
                );
                file << endl;

                -- Print to fileLevel
                fileLevel << "p = " << toString(p);
                if isIrred then (
                    fileLevel << ", irred = true ";
                ) else (
                    fileLevel << ", irred = false";
                );
                fileLevel << ", level = " << toString(out_0) << endl;
            );
        );
        file << close;
        fileLevel << close;
    );
);
