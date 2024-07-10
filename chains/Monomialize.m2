
monomialize = method();

-- Parameters;
--      - N     number of indeterminates
--      - pe    e-th power of p
--      - a     an list of non-negative integers a = (a_0, ..., a_(N-1))
--      - ve    list of powers of p^e, ve = ( (p^e)^(N-1), (p^e)^(N-2), ..., p^e, 1)

-- The function does:
--      - For each i, the function computes a_i = b_i p^e + r_i, with b_i >= 0 and 0 <= r_i < p^e

-- Return:
--      - b     list b = (b_0, ..., b_(N-1))
--      - r     list r = (r_0, ..., r_(N-1))
--      - bel   Basis ELement, i.e. the integer r_0 * ve_0 + r_1 * ve_1 + ... + r_(N-1) * ve_(N-1)

monomialize(ZZ, List, List) := (pe, a, ve) -> (

    -- print("Here");

    b := {};
    r := {};
    xb := 1;
    bel := 0;

    for i from 0 to (length a - 1) do (

        ai := a#i;
        bi := floor(ai / pe);   
        ri := ai % pe;
        ti := bi * pe + ri;
        b = append(b, bi);
        r = append(r, ri);
        bel = bel + ri * ve#i;
        -- print(concatenate(toString(ai), " ", toString(bi), " ", toString(ri), " ", toString(ti)));
        xb = xb * x_(i+1)^bi;

    );

    return (xb, r, bel);

);