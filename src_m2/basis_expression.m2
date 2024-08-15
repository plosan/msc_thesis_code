load "packages/Chains.m2"
load "packages/Monomialize.m2"
load "packages/NewFrobeniusRoots.m2"

-- Setup
p = 11
R = ZZ/p[x, y]
e = 1   -- Frobenius roots order
N = 2   -- Number of variables
varList = {x, y};

-- Polynomial
t1 = 1
t2 = 1
f = x^4 + y^7 + t1 * x^2 * y^4 + t2 * x^2 * y^5

for r from 0 to p - 1 do (
    expr = basisExpression(f^r, p, e);
    print(concatenate("\ne = ", toString(e)));
    print(expr);
);
