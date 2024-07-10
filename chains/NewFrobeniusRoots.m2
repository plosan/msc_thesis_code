
newFrobeniusRootPrincipal = method();
newFrobeniusRoot = method();

newFrobeniusRootPrincipal(RingElement, ZZ, List) := (f, pe, ve) -> (
    
    -- Monomials of f and their Coefficients
    (M, C) := coefficients f;   

    -- List of generators of the Frobenius root of f
    fRootGenList := {}; 

    -- Loop through all the monomials of f
    for j from 0 to (numColumns(M) - 1) do (
        -- print exponentsMonomial;
        -- Compute the monomial in the standard basis
        exponentsMonomial = (exponents M_(0,j))#0;                  -- Exponents of the monomial
        (xb, r, bel) := monomialize(pe, exponentsMonomial, ve);  -- Compute monomial in the basis
        xb = xb * C_(j,0);

        -- Integrate monomial in the set of generators of the Frobenius root of f
        -- First look if there is already some monomial with the same basis element (same bel)
        k := 0;
        found := false;
        while(found == false and k < length fRootGenList) do (
            genk := fRootGenList#k;
            if (bel == genk#0) then (
                found = true;
                xb = xb + genk#1;
                fRootGenList = drop(fRootGenList, {k,k});
                fRootGenList = append(fRootGenList, {bel, xb});
                -- fRootGenList#k = {bel, genk#1 + xb};
            );
            k = k + 1;
        );
        -- If there is no monomial with the same basis element, append element to the list
        if (found == false) then (
            fRootGenList = append(fRootGenList, {bel, xb});
        );
    );

    -- Return generators of the Frobenius root
    return fRootGenList;
);

newFrobeniusRoot(ZZ, Ideal) := (e, I) -> (

    -- Create vector of powers of p^e, ( (p^e)^(N-1), (p^e)^(N-2), ..., (p^e), 1)
    ve := {1};
    for i from 0 to (N - 2) do (
        ve = prepend(p * ve#0, ve);
    );

    -- Lists of generators
    genIdeal := first entries gens I;   -- Generators of I
    genList := {};                      -- Generators of the Frobenius root

    for i from 0 to (length genIdeal - 1) do (
        -- i-th generator of I
        f := genIdeal#i;
        fRootGenList := newFrobeniusRootPrincipal(f, pe, ve);
        -- Merge lists
        for j from 0 to (length fRootGenList - 1) do (
            gen := fRootGenList#j;
            genList = append(genList, gen#1);      
        );
    );

    -- Return Frobenius root
    J := ideal unique(genList);
    return J;

);