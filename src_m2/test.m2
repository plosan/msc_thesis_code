loadPackage "TestIdeals"
load "packages/NewFrobeniusRoots.m2"

p = 43
R = ZZ/p[x, y]
f = y^2 - x^3
g = f^2 - x^5 * y

gpower = 1
for r from 1 to p-1 do (
	gpower = g * gpower;
	-- be := basisExpression(gpower, 1);
	print(concatenate("\n\nr = ", toString(r), "\tideal = ", toString(frobeniusRoot(1, ideal(gpower)))));
	-- print(concatenate("\n\nr = ", toString(r)));
	-- print(concatenate("ideal = ", toString(frobeniusRoot(1, ideal(gpower)))));
	-- print(concatenate("ideal = ", toString(be)));
);
