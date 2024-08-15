import sys

def get_exponents_monomials_deformation(a, b):
    """Computes the exponents x^i * y^j of the monomials that give a deformation of
    the polynomial x^a + y^b with constant Milnor number.

    Args:
        a (int): exponent of x in x^a.
        b (int): exponent of y in y^b.

    Returns:
        exponents (list of 2-tuples of ints): tuples (i, j) such that x^i * y^j gives
        a deformation of x^a + y^b with constant Milnor number.
    """
    exponents = [(i, j) for i in range(a - 1) for j in range(b - 1) if a * j + b * i > a * b]
    return exponents

def _indeterminate_power_to_string(var, i):
    """Returns a string of the variable ``var`` raised to the power of ``i``.
    """
    if i == 0:
        return ''
    if i == 1:
        return var
    return f'{var}^{i}'

def exponents_to_string(i, j, c):
    """Returns the term c * x^i y^j converted to a string.

    Args:
        i (int): exponent of x.
        j (int): exponent of y.
        c (int): coefficient multiplying the monomial x^i y^j.

    Returns:
        out (str): the monomial c * x^i y^j converted to a string.    
    """
    # Parse coefficient string
    str_coef = ''   # Coefficient string
    if isinstance(c, str):
        str_coef = c
    elif isinstance(c, int):
        if c == 0:
            return '0'
        else:
            str_coef = str(c)
    else:
        raise ValueError("Argument 'c' in function 'exponents_to_string(i, j, c)' must either be 'str' or 'int'.")
    # Parse indeterminate strings
    str_x = _indeterminate_power_to_string('x', i)  # x string
    str_y = _indeterminate_power_to_string('y', j)  # y string
    # Build term
    if str_x == '' and str_y == '': # A constant term
        return str_coef
    if str_coef == '1':             # Non-constant term with coefficient 1
        str_coef = ''
    out = [str_coef, str_x, str_y]
    out = [elem for elem in out if elem != '']
    out = ' '.join(out)
    return out


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print('Invalid number of parameters. Run the script like python3 monomials_of_deformation a b')
        sys.exit(0)

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    # Polynomial
    pol_term_str = [exponents_to_string(a, 0, 1), exponents_to_string(0, b, 1)]
    pol_str = ' + '.join(pol_term_str)

    # Terms of deformation
    exponents_def = get_exponents_monomials_deformation(a, b)
    def_term_str = [exponents_to_string(*elem, f't{elem[0]}{elem[1]}') for elem in exponents_def]

    # Deformation
    def_str = pol_term_str + def_term_str
    def_str = ' + '.join(def_str)

    print(f"{'%15s' %('Polynomial')}: {pol_str}")
    print(f"{'%15s' %('Deformation')}: {def_str}")