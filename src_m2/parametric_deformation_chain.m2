load "packages/Chains.m2"

a = 7;
b = 4;
minPrime = 2;
maxPrime = 100;

-- Find primes in range [minPrime, maxPrime] such that p = 1 or p = -1 mod (a * b) 
primeList = {};
for p from 2 to 100 do (
    if not isPrime(p) then (
        continue;
    );
    if not (p % (a * b) == 1 or p % (a * b) == a * b - 1) then (
        continue;
    );
    primeList = append(primeList, p);
);


for idx from 0 to (length primeList - 1) do (

    p := primeList#idx;

    filename := concatenate("parametric_", toString(a), "_", toString(b), "_p", toString(p), ".txt");
    file := concatenate("../data/parametric_deformation_r_chain/", filename);
    file << filename << endl << close;

    print(concatenate("p = ",  toString(p)));

    -- Parametric deformation
    R := GF(p)[x, y, t1, t2];
    f := x^4 + y^7 + t1 * x^2 * y^4 + t2 * x^2 * y^5;
    isIrred := isPrime(f);

    -- Parametric r chain
    out = rChainVerbose(f, 1);
    nuInv := out_0;
    fRoots := out_1;

    -- Print parametric chain to file
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

);
