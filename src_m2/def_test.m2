load "packages/Deformation.m2"
load "packages/Chains.m2"

a = 5
b = 7
defMonList = getDeformationMonomials(a, b);

p = 71
R = GF(p)[x, y]
f = x^5 + y^7
g = f

for i from 0 to length(defMonList) - 1 do (
    mon = defMonList#i;
    alpha = mon#0;
    beta = mon#1;
    g = g + x^alpha * y^beta;
)

print(concatenate("f = ", toString(f)))
rChainVerbose(f, 1)

print(concatenate("\ng = ", toString(g)))
rChainVerbose(g, 1)

