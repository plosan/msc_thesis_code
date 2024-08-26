loadPackage "TestIdeals"
-- load "packages/Chains.m2"

for p from 2 to 100 do (

    if not isPrime(p) then (
        continue;
    );

    print(concatenate("\np = ", toString(p)));

    R = GF(p)[x, y];

    -- h = x^2 * y^5 + x^3 * y^3 + x^3 * y^4 + x^3 * y^5

    f = x^5 + y^7;
    h = x^7;
    g = f + h;
    -- x^5+y^7 + t1 * x^2 * y^5 + t2 * x^3 * y^3 + t3 * x^3 * y^4 + t4 * x^3 * y^5
    fpower = 1;
    gpower = 1;
    hpower = 1;

    for r from 1 to p - 1 do (
        fpower = f * fpower;
        gpower = g * gpower;
        hpower = h * hpower;
        rootf = frobeniusRoot(1, ideal(fpower));
        rootg = frobeniusRoot(1, ideal(gpower));
        rooth = frobeniusRoot(1, ideal(hpower));
        
        if not isSubset(rootf, rootg) then (
            print(concatenate("Subset f, r = ", toString(r)));
        );

        if not isSubset(rooth, rootg) then (
            print(concatenate("Subset h, r = ", toString(r)));
        );

    );
    
)