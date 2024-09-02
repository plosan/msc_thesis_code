import copy
import math
import settings

def line_func(line, point):
    """Evaluates the expression a x + b y - c, where line = (a, b, c) 
    and point = (x, y).

    Args:
        line (tuple): Coefficients a, b, c of the line.
        point (tuple): (x, y) coordinates of a point.

    Returns:
        float: Value a x + b y - c. 
    """
    a, b, c = line
    x, y = point
    return a * x + b * y - c

def plot_binomial_line(ax, a, b, c, **kwargs):
    """Plots the line a x + b y = c in the first quadrant on the provided axes object. It is 
    therefore assumed that a, b, c are strictly positive real numbers.
    Args:
        ax (matplotlib.axes._axes.Axes): axis where the line will be plotted.
        a (float): positive real number, coefficient of x in the line equation.
        b (float): positive real number, coefficient of y in the line equation.
        c (float): positive real number, independent term in the line equation.
        **kwargs (dict): ax.plot kwargs parameter.
    Returns:
        None
    Raises:
        ValueError: if either a, b or c are <= 0.
    """
    if not all([a > 0, b > 0, c > 0]):
        raise ValueError("Parameters a, b, c for line a x + b y = c must be > 0")
    x_coords = [0, c/a]
    y_coords = [c/b, 0]
    ax.plot(x_coords, y_coords, **kwargs)
    
def p_adic_expansion(p, m):
    """Computes the p-adic expansion [c0, c1, ..., cn] of a non-negative
    integer m, where p is a positive integer not necessarily prime. The
    p-adic expansion satisfies the following:
    c0 + c1 * p^1 + ... + cn * p^n = m.

    Args:
        p (int): Positive integer, base.
        m (int): Positive integer, number whose p-adic expansion is to 
            be computed.

    Returns:
        list: Coefficients [c0, c1, ..., cn] of the p-adic expansion, 
    """
    if m == 0:
        return [0]
    
    aux = m
    coefs = []
    while aux > 0:
        c = aux % p
        coefs.append(c)
        aux = (aux - c) // p
    return coefs

def p_adic_expansion_check(p, m, coefs, verbose=True):
    """Verifies tgat the p-adic expansion of m was computed correctly.
    Used for debugging purposes.

    Args:
        p (int): Positive integer, base.
        m (int): Positive integer, number whose p-adic expansion is to 
            be verified.
        coefs (list of int): Coefficients of the p-adic expansion of m.
        verbose (bool, optional): If the p-adic expansion is wrong, it 
            prints it on screen. Defaults to True.

    Returns:
        bool: Whether or not the p-adic expansion is pro
    """
    # Compute the number c0 + c1 * p^1 + ... + cn * p^n
    aux = 0
    p_power = 1
    for coef in coefs:
        aux = aux + p_power * coef
        p_power = p * p_power
    # Compute c0 + c1 * p^1 + ... + cn * p^n - m
    diff = aux - m
    if diff != 0 and verbose:
        print(f'Incorrect p-adic expansion: diff = {diff}')
    return diff == 0

def is_prime(p, primes_list=None):
    """Whether or not the argument p is a prime number. 
    
    If the argument primes_list is provided, it checks whether or not p 
    is in the list, as long as p is smaller than the largest prime in
    the list.

    Args:
        p (int): Integer whose primality is to be checked
        primes_list (list, optional): List of prime numbers. Defaults 
            to None.

    Returns:
        bool: Whether or not p is prime.
    """
    if primes_list is not None:
        if primes_list[-1] >= p:
            return p in primes_list
        
    for n in range(2, math.floor(math.sqrt(p)) + 1):
        if p % n == 0:
            return False
        
    return True

def load_primes():
    """Loads the prime numbers in the file settings.PRIMES_FILE.

    Returns:
        list: Prime numbers in the file settings.PRIMES_FILE.
    """
    with open(settings.PRIMES_FILE, 'r') as file:
        primes_list = [int(line.strip()) for line in file]
    return primes_list

def find_primes_congruent(a, cong, primes_list=None):
    """Finds the primes congruent that modulo a are congruent to:
        * cong, if cong is an integer
        * an element in cong, if cong is array_like

    Args:
        a (int): Integer with respect which the congruence is computed.
        cong (int or array like): Target of the congruence mod a.
        primes_list (list, optional): List of primes that are tested for
            congruence. If not provided, the primes in 
            data/prime_numbers/primes.txt are loaded. Defaults to None.

    Returns:
        array_like: List of primes in prime_list congruent to an element
            in cong modulo a.
            
    Raises:
        ValueError: if cong is not an instance of int, list or tuple
    """
    # Set up admissible congruences list
    _cong_list = cong
    if isinstance(_cong_list, int):
        _cong_list = [_cong_list]
    elif isinstance(_cong_list, list) or isinstance(_cong_list, tuple):
        _cong_list = list(_cong_list)
    else:
        raise ValueError("Argument 'cong' must be an instance of int or array_like")
    # Load primes in data/prime_numbers/primes.txt if not provided
    _primes_list = primes_list
    if _primes_list is None:
        _primes_list = load_primes()
    # Make elements in _cong_list be in the [0, a-1] range
    _cong_list = [b % a for b in _cong_list]
    # Find primes congruent to something in cong
    primes_cong = [p for p in _primes_list if p % a in _cong_list]
    return primes_cong

def mu_const_def_monomials(a, b):
    line_params = (b, a, a * b)
    mon_def = [(i, j) for i in range(a-1) for j in range(b-1) if line_func(line_params, (i,j)) > 0]
    return mon_def

def mu_const_def_monomials_values(a, b, def_mon=None):
    _def_mon = def_mon
    if _def_mon is None:
        _def_mon = mu_const_def_monomials(a, b)
    
    values_mon = dict()
    line = (b, a, 0)
    for mon in _def_mon:
        val = line_func(line, mon)
        if val not in values_mon:
            values_mon[val] = [mon]
        else:
            values_mon[val].append(mon)
    return values_mon

def generate_monomials(n, deg):
    """Generates the exponents of all the monomials in n variables of 
    degree deg. There are n+d-1 choose d monomials of these kind. 

    Args:
        n (int): Number of variables of the monomial, positive integer.
        deg (int): Degree of the monomials, positive integer.

    Returns:
        mon_list: List of all the monomials of degree d, sorted in 
            lexicographic order. Each monomial is represented by a tuple
            of length n.
    """
    mon_list = []
    mon_exp = [0 for i in range(n)]
    _recursive_gen_mon(mon_list, mon_exp, deg, 0, 0)
    mon_list = [tuple(mon) for mon in mon_list]
    return mon_list
    

def _recursive_gen_mon(mon_list, mon_exp, deg, sum, i):
    """Recursive call to function ``generate_monomials''.

    Args:
        mon_list (list): List where the monomials of degree deg in 
            len(mon_exp) variables are stored.
        mon_exp (list): Exponents of the monomial of degree deg.
        deg (int): Target degree of the monomial.
        sum (int): Current sum of the exponents in the monomial.
        i (int): Variable whose exponent will be set in this recursive
            call.
    """
    if sum == deg:
        mon_list.append(copy.copy(mon_exp))
        return
    
    if i == len(mon_exp) - 1:
        mon_exp[-1] = deg - sum
        _recursive_gen_mon(mon_list, mon_exp, deg, deg, i+1)
        mon_exp[-1] = 0
        return
        
    for k in range(deg - sum + 1):
        mon_exp[i] = k
        _recursive_gen_mon(mon_list, mon_exp, deg, sum+k, i+1)
        mon_exp[i] = 0
    
def compute_min_gen_set(monomial_list):
    """Computes the minimal set of generators of a monomial ideal in a
    polynomial ring in two variables.

    Args:
        monomial_list (list): List containing the exponents of the
            monomials as tuples. Example: [(0,2), (1,3), (0,3)].

    Returns:
        vertices (list): Minimal generating set for the monomial ideal.
    """
    if not monomial_list:
        return None
    
    _monomial_list = [tuple(monomial) for monomial in monomial_list]
    _monomial_list.sort()
    vertices = [_monomial_list[0]]
    for monomial in _monomial_list[1:]:
        if monomial[0] > vertices[-1][0] and monomial[1] < vertices[-1][1]:
            vertices.append(monomial)
            
    return vertices