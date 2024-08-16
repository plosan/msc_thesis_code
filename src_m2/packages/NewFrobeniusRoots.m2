
basisExpression = method();
newFrobeniusRootPrincipal = method();
newFrobeniusRoot = method();

nonzero = x -> x != 0

basisExpression(RingElement, ZZ) := (f, e) -> (
    -- Computes the coefficients of f in the basis {F^e x1^i1...xn^in | 0 <= i1, ..., in < p^e} of 
    -- the free R-module F^e R, where R = Fp[x1, ..., xn] is a polynomial ring over Fp = ZZ/p.
    -- Args:
    --      f (RingElement): a polynomial.
    --      e (ZZ): exponent of p, p = char(R).
    -- Returns:
    --      basisExpression (set): coefficients of f in the basis.
    -- Warning: only works for polynomial rings R = Fp[x1, ..., xn].

    R := ring(f);
    print("here");
    if not instance(R, PolynomialRing) then (
        print("Error: ring must be a polynomial ring");
        return;
    );
    if not isFinitePrimeField(coefficientRing(R)) then (
        print("Error: coefficient ring must be a finite field ZZ/p");
        return;
    );

    -- Polynomial ring variables
    p = char(R);
    q := p^e;
    varList := gens(R);
    N := length(varList);

    -- Monomials and coefficients of f
    (monList, coefList) := coefficients(f);
    monList = (entries(monList))_0;
    coefList = entries(coefList)_0;
    monCount := length(monList);
    -- Basis expression of f
    basisExpression := 0 * toList(0..q^N-1);
    basisExpression = new MutableList from basisExpression;

    for i from 0 to monCount - 1 do (
        -- Monomial and coefficient
        coef := coefList#i;             -- Coefficient
        mon := monList#i;               -- Monomial
        exps := (exponents(mon))_0;     -- Monomial exponents
        -- Exponents of the basis element and exponents of the monomial that multiplies it
        basisElementId := 0;
        coefficientMonomial := coef;
        for j from 0 to length(exps) - 1 do (
            -- Exponent
            exponent := exps#j;
            -- Update basis element number
            emod := exponent % q;
            basisElementId = q * basisElementId + emod;
            -- Update monomial that multiplies the basis element
            efloor := floor(exponent / q);
            coefficientMonomial = coefficientMonomial * (varList#j) ^ efloor;
        );
        -- Update basis expression
        basisExpression#basisElementId = basisExpression#basisElementId + coefficientMonomial;
    );
    -- Remove zeros and repeated elements from the basis expression
    basisExpression = set(toList((select(basisExpression, nonzero))));
    return basisExpression;
);

newFrobeniusRootPrincipal(RingElement, ZZ, List) := (f, pe, ve) -> (
    
    -- Monomials of f and their Coefficients
    (M, C) := coefficients f;   

    -- List of generators of the Frobenius root of f
    fRootGenList := {};

    -- Loop through all the monomials of f
    for j from 0 to (numColumns(M) - 1) do (
        -- print exponentsMonomial;
        -- Compute the monomial in the standard basis
        exponentsMonomial := (exponents M_(0,j))#0;                  -- Exponents of the monomial
        (xb, r, bel) := monomialize(pe, exponentsMonomial, ve);  -- Compute monomial in the basis
        continue;
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