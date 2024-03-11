from sage.all import *

def _have_same_length(a, *args):
    """Checks if argument ``a`` and the elements in ``*args`` have the same len.

    Args:
        a (list, tuple or set): A list, tuple or set whose length has to be compared to the lengths of elements in ``*args``.
        *args (tuple of lists, tuples, sets): Elements whose lengths have to be compared to len

    Returns:
        out (bool): ``True`` if ``len(a)`` is equal to ``len(elem)`` for each ``elem`` in ``*args``, ``False`` otherwise. 
    """
    if len(args) == 0:
        return True
    ref_len = len(a)
    for elem in args:
        if ref_len != len(elem):
            return False
    return True

def _check_monomialize(pe, exponents, coefs, bases):
    if not _have_same_length(exponents, coefs, bases):
        raise ValueError("Something's up dude")
    for i in range(len(exponents)):
        if exponents[i] != coefs[i] * pe + bases[i]:
            return False
    return True
    
def _monomialize(pe, exponents):
    """Computes the expression in the standard basis of the R-module F^e R of the monomial with the given exponents.
    
    Args:
        pe (int): Characteristic p to the e-th power, i.e p^e
        exponents (list or tuple of ints): Exponents of the monomial
        
    Returns:
        coef (tuple of ints): Coefficient in the basis.
        base (tuple of ints): Exponents of the monomial of the basis element.
    """
    coef = tuple([exponent // pe for exponent in exponents])
    base = tuple([exponent % pe for exponent in exponents])
    return coef, base

def _monomialize_polynomial(pe, f, gens):
    expression = dict()
    f_coefs = f.coefficients()
    f_exps = f.exponents()
    for i in range(len(f_coefs)):
        coef, basis_elem = _monomialize(pe, f_exps[i])
        monomial = f_coefs[i] * _exponents_to_monomial(coef, gens)
        if basis_elem not in expression:
            expression[basis_elem] = [monomial]
        else:
            expression[basis_elem].append(monomial)
    return expression
    
    # a = list(expression.values())
    # a = [[] for elem in a]

def _exponents_to_monomial(exponents, gens):
    f = 1
    for i in range(len(exponents)):
        f *= gens[i] ** exponents[i]
    return f

# def _check_if_monomial(f):

def frobenius_root(p, e, f):
    gens = f.parent().gens()
    expression = _monomialize_polynomial(p**e, f, gens)
    expression = list(expression.values())
    # for elem in expression:
    #     print(elem)
    #     print(sum(elem))
    #     print()
    # froot_gens = set[sum(elem) for elem in expression]
    froot_gens = set([sum(elem) for elem in expression])
    return ideal(list(froot_gens))

def frobenius_root_ideal(p, e, a):
    ideal_gens = a.gens()
    froot_elems = [frobenius_root(p, e, elem) for elem in ideal_gens]
    froot = froot_elems[0]
    for i in range(1, len(froot_elems)):
        froot += froot_elems[i]
    

def compute_nu_invariants(p, e, f, nu_inv_count = 10):
    """Computes the nu-invariants of level e of the polynomial f.

    Args:
        p (int): Characteristic of the ring.
        e (int): Level of the nu-invariants.
        f (polynomial): Polynomial whose nu-invariants are to be computed.
        nu_inv_count (int, optional): Number of nu-invariants to be computed. Defaults to 10.
    
    Returns:
        nu_invariants (list of ints): List with the first ``nu_inv_count`` nu-invariants of level e of f.        
    """

    nu_invariants = []
    f_power = f
    pe = p ** e
    current_froot = frobenius_root(pe, f_power)

    if not f.parent().ideal(1) <= current_froot:
        nu_invariants.append(0)

    count = len(nu_invariants)
    n = 1
    while count < nu_inv_count:
        f_power *= f
        n += 2
        next_froot = frobenius_root(p, e, f_power)
        if not current_froot <= next_froot:
            nu_invariants.append(n)
            current_froot = next_froot
            count += 1
            print(count, n)
    return nu_invariants