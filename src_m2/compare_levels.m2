load "Chains.m2"

for p from 2 to 100 do (
    if isPrime(p) then (
        R := GF(p)[x, y, t];
        f := x^4 + y^5;
        out = eChain(f, 10);
        -- print(concatenate("f = ", toString(f)));
        print(concatenate("p = ", toString(p)));
        print(concatenate("level = ", toString(out_0)));
        g := x^4 + y^5 + t * x^2 * y^3;
        out = eChain(g, 10); 
        -- print(concatenate("g = ", toString(g)));
        print(concatenate("level = ", toString(out_0)));
        print("");
    );
);