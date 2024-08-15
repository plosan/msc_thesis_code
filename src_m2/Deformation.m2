

getDeformationMonomials = method();
getDeformationMonomials(ZZ, ZZ) := (a, b) -> (
    -- Computes the exponents (i0,j0), ..., (in,jn) of the monomial x^i * y^j 
    -- such that x^a + y^b + t0 x^i0 y^j0 + ... + tn x^in y^jn is a deformation 
    -- of x^a + y^b with the same Milnor number. These monomials satisfy that
    -- i < a - 1, j < b - 1 and a j + b i > a b. 
    -- Args:
    --      a (ZZ): Exponent of x in x^a + y^b.
    --      b (ZZ): Exponent of y in x^a + y^b.
    -- Returns:
    --      defMonList (List): List containing sequences (i,j) such that x^i y^j
    --      is a monomial satisfying the conditions above.
    defMonList := {};
    ab := a * b;
    for i from 0 to a - 2 do (
        for j from 0 to b - 2 do (
            if a * j + b * i > ab then (
                defMonList = append(defMonList, (i, j));
            );
        );
    );
    return defMonList;
);