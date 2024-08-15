-- Script to compute and save to a file the deformations of binomial x^a + y^b
-- that preserve the Milnor number. These deformations have the form
-- x^a + y^b + t0 x^i0 y^j0 + ... + tn x^in y^jn, where the exponents (i,j) 
-- satisfy i < a - 1, j < b - 1 and a j + b i > a b.
-- It saves the output to the file "../out/deformation_data/deformations.txt".
load "Deformation.m2"

defFile = "../out/deformation_data/deformations.txt";   -- Output file
aMax = 20   -- Maximum exponent x^a
bMax = 20   -- Maximum exponent y^b

for a from 3 to aMax do (
    for b from a to bMax do (
        defMon := getDeformationMonomials(a, b);
        R := QQ[t_1..t_(length defMon), x, y, MonomialOrder => Lex];
        f := x^a + y^b;
        g := 0;
        for i from 0 to (length defMon - 1) do (
            mon = defMon#i;
            g = g + t_(i+1) * x^(mon#0) * y^(mon#1);
        );
        defFile << "exp " << toString(a) << "," << toString(b) << endl;
        defFile << "pol " << toString(f) << endl;
        defFile << "mon";
        for mon in defMon do (
            defFile << " " << toString(mon);
        );
        defFile << endl;
        defFile << "def " << toString(f) << " + " << toString(g) << endl << endl;
        -- print(f);
        -- print(concatenate(toString(f), " + ", toString(g)));
    );
);
defFile << close;