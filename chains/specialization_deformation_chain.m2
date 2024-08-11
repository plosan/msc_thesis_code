load "Chains.m2"

-- x^4+y^7 + t_1 * x^2 * y^4 + t_2 * x^2 * y^5

a = 4
b = 7
ab = a * b

for p from 2 to 200 do (
    if not isPrime(p) then (
        continue;
    );
    if not (p % (ab) == 1 or p % (ab) == ab - 1) then (
        continue;
    );
    -- Setup
    R = GF(p)[x, y, t1, t2];
    f = x^4 + y^7 + x^2 * y^4 + x^2 * y^5;
    g = x^4 + y^7 + t1 * x^2 * y^4 + t2 * x^2 * y^5;

    -- Compute chain for f
    print(concatenate("\n\n----------\np = ", toString(p)));

    print(concatenate("\nf = ", toString(f)));
    rChainVerbose(f, 1);

    -- -- Compute chain for g
    print(concatenate("\ng = ", toString(g)));
    rChainVerbose(g, 1);

);