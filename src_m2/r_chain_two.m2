load "../chains/Chains.m2"

polyName = "(y^2 - x^3)^2 - x^5 * y"
file = "../out/two_char_exps/poly1.txt";
-- file << polyName << endl << close;

for p from 100 to 500 do (
    if not isPrime(p) then (
        continue;
    );
    if not (p % 6 == 1) then (
        continue;
    );
    -- Setting
    R = GF(p)[x, y];
    f = (y^2 - x^3)^2 - x^5 * y;
    isIrred := isPrime(ideal(f));
    -- Printing
    print(concatenate("\np = ", toString(p)));
    print(concatenate("irred = ", toString(isIrred)));
    -- Computations
    out = rChainVerbose(f, 1);
    nuInv = out#0;
    fRoots = out#1;
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
);