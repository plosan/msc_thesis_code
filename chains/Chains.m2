loadPackage "TestIdeals"

rChain = method();
rChain(RingElement, ZZ) := (f, e) -> (
    -- Computes the ideals in the chain of Frobenius roots
    -- (f)^[1 / p^e] \supseteq (f^2)^[1 / p^e] \supseteq ... 
    -- \supseteq (f^(p^e - 1))^[1 / p^e] and the nu-invariants. 
    -- Args:
    --      f (RingElement): polynomial for which the chain is computed.
    --      e (ZZ): exponent of the Frobenius roots.
    -- Returns:
    --      nuInvList (List): list of the nu-invariants in 1, 2, ..., p^e - 1.
    --      fRootList (List): distinct Frobenius roots in the chain above.
    p := char(ring(f)); -- Characteristic of the ring
    rmax := p^e - 1;    -- Max power of f for which a Frobenius roots is computed
    auxRoot := frobeniusRoot(e, ideal(f));  -- Auxiliary Frobenius root
    fpower := f;                -- Power of f
    fRootList := {auxRoot};     -- List of the distinct e-th Frobenius roots
    nuInvList := {};            -- List of nu-invariants of level e

    -- Compute Frobenius roots, linearly
    for r from 2 to rmax do (
        fpower = fpower * f;
        root := frobeniusRoot(e, ideal(fpower));
        if not isSubset(auxRoot, root) then (
            fRootList = append(fRootList, root);
            nuInvList = append(nuInvList, r - 1);
            auxRoot = root;
        );
    );
    nuInvList = append(nuInvList, rmax);    -- p^e - 1 is always a nu-invariant

    return (nuInvList, fRootList);
);

rChainVerbose = method();
rChainVerbose(RingElement, ZZ) := (f, e) -> (
    -- Computes the ideals in the chain of Frobenius roots
    -- (f)^[1 / p^e] \supseteq (f^2)^[1 / p^e] \supseteq ... 
    -- \supseteq (f^(p^e - 1))^[1 / p^e] and the nu-invariants. Prints the 
    -- process on the screen.
    -- Args:
    --      f (RingElement): polynomial for which the chain is computed.
    --      e (ZZ): exponent of the Frobenius roots.
    -- Returns:
    --      nuInvList (List): list of the nu-invariants in 1, 2, ..., p^e - 1.
    --      fRootList (List): distinct Frobenius roots in the chain above.
    p := char(ring(f)); -- Characteristic of the ring
    rmax := p^e - 1;    -- Max power of f for which a Frobenius roots is computed
    auxRoot := frobeniusRoot(e, ideal(f));  -- Auxiliary Frobenius root
    fpower := f;                -- Power of f
    fRootList := {auxRoot};     -- List of the distinct e-th Frobenius roots
    nuInvList := {};            -- List of nu-invariants of level e
    rprev = 1;                  -- Variable for printing purposes, equal to the previous nu-invariant + 1

    -- Compute Frobenius roots, linearly
    for r from 2 to rmax do (
        fpower = fpower * f;
        root := frobeniusRoot(e, ideal(fpower));
        if not isSubset(auxRoot, root) then (
            -- Printing part
            print(concatenate("[", toString(rprev), ", ", toString(r - 1), "]: ", toString(auxRoot)));
            rprev = r;
            -- 
            fRootList = append(fRootList, root);
            nuInvList = append(nuInvList, r - 1);
            auxRoot = root;
        );
    );
    nuInvList = append(nuInvList, rmax);    -- p^e - 1 is always a nu-invariant

    return (nuInvList, fRootList);
);

eChain = method();
eChain(RingElement, ZZ) := (f, emax) -> (
    -- Computes the ideals in the chain of Frobenius roots
    -- (f^(p - 1))^[1 / p] \supseteq (f^(p^2 - 1))^[1 / p^2] \supseteq ... 
    -- \supseteq (f^(p^e - 1))^[1 / p^e] until e == emax or stabilization, 
    -- whichever occurs first. Stabilization occurs when two (consecutive)
    -- Frobenius roots are equal. It also computes the level of the singularity, 
    -- i.e. the integer where the chain stabilizes.
    -- Args:
    --      f (RingElement): polynomial for which the chain is computed.
    --      emax (ZZ): maximum exponent of the Frobenius roots.
    -- Returns:
    --      level (ZZ): level of the singularity, or -1 if it is emax < level.
    --      fRootList (List): Frobenius roots in the chain above.
    p := char(ring(f)); -- Characteristic of the ring
    auxRoot := frobeniusRoot(1, ideal(f^(p - 1)));  -- Auxiliary Frobenius root
    fRootList := {auxRoot};                         -- List of Frobenius roots computed above

    if auxRoot == 1 then (  -- The level is zero
        return (0, fRootList);
    );

    e := 2;         -- Level of the Frobenius root (f^(p^e - 1))^[1 / p^e]
    level := -1;    -- Level of the singularity. Is kept to -1 to check for stabilization
    while (e <= emax) and (level == -1) do (
        fpower := f^(p^e - 1);
        root := frobeniusRoot(e, ideal(fpower));
        if isSubset(auxRoot, root) then (   -- Stabilized!
            level = e - 1;
        ) else (
            fRootList = append(fRootList, root);
            auxRoot = root;
        );
        e = e + 1;
    );

    return (level, fRootList);
);

eChainVerbose = method();
eChainVerbose(RingElement, ZZ) := (f, emax) -> (
    -- Computes the ideals in the chain of Frobenius roots
    -- (f^(p - 1))^[1 / p] \supseteq (f^(p^2 - 1))^[1 / p^2] \supseteq ... 
    -- \supseteq (f^(p^e - 1))^[1 / p^e] until e == emax or stabilization, 
    -- whichever occurs first. Stabilization occurs when two (consecutive)
    -- Frobenius roots are equal. It also computes the level of the singularity,
    -- i.e. the integer where the chain stabilizes. Prints the process on the screen.
    p := char(ring(f)); -- Characteristic of the ring
    -- Args:
    --      f (RingElement): polynomial for which the chain is computed.
    --      emax (ZZ): maximum exponent of the Frobenius roots.
    -- Returns:
    --      level (ZZ): level of the singularity, or -1 if it is emax < level.
    --      fRootList (List): Frobenius roots in the chain above.
    auxRoot := frobeniusRoot(1, ideal(f^(p - 1)));  -- Auxiliary Frobenius root
    fRootList := {auxRoot};                         -- List of Frobenius roots computed
    -- Print
    print(concatenate("e = ", toString(1), "\tIdeal : ", toString(auxRoot)));
    -- 
    if auxRoot == 1 then (  -- The level is zero
        return (0, fRootList);
    );
    e := 2;         -- Level of the Frobenius root (f^(p^e - 1))^[1 / p^e]
    level := -1;    -- Level of the singularity. Is kept to -1 to check for stabilization
    while (e <= emax) and (level == -1) do (
        fpower := f^(p^e - 1);
        root := frobeniusRoot(e, ideal(fpower));
        -- Print
        print(concatenate("e = ", toString(e), "\tIdeal : ", toString(root)));
        if isSubset(auxRoot, root) then (   -- Stabilized!
            level = e - 1;
        ) else (
            fRootList = append(fRootList, root);
            auxRoot = root;
        );
        e = e + 1;
    );
    -- Print
    print(concatenate("Level = ", toString(level)));

    return (level, fRootList);
);
