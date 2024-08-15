
def _dot_product(a, b):
    # Computes the dot product of the vectors a and b. The vectors are assumed to have the same length
    return sum([a[i] * b[i] for i in range(len(a))])

def is_monomial(elem_str):
    if '+' in elem_str:
        return False
    if '-' in elem_str:
        return False
    return True

def str_to_monomial(mon_str):

    sign = 1
    mon_str = mon_str.strip()
    if mon_str[0] == '-':
        sign = -1
        mon_str = mon_str[1:]

    parts = [part.strip() for part in mon_str.split('*')]
    
    coef = 1
    exp_x = 0
    exp_y = 0

    for part in parts:
        if 'x' in part:     # part with x; it has the form x^n
            exp_x = int(part[2:]) if '^' in part else 1
        elif 'y' in part:   # part with y; it has the form x^m
            exp_y = int(part[2:]) if '^' in part else 1
        else:               # coefficient
            coef = sign * int(part)
    
    return Monomial(coef, [exp_x, exp_y])

def exponent_to_variable_str(var_char, exp):
    if exp == 0:
        return ''
    if exp == 1:
        return var_char
    return f'{var_char}^{str(exp)}'



class Monomial:
    def __init__(self, coef : int, exp : list):
        if not isinstance(coef, int):
            raise ValueError("Argument 'coef' in Monomial constructor must be an int")
        if not isinstance(exp, list):
            raise ValueError("Argument 'exp' in Monomial constructor must be a list or a tuple")
        if not all([isinstance(elem, int) for elem in exp]):
            raise ValueError("Argument 'coef' in Monomial constructor must be a list or a tuple")
        
        self.coef = coef            # coefficient of the monomial (yes, it should be called term, I know)
        self.exp = tuple(exp)       # exponents
        self.nvar = len(self.exp)   # number of variables

    def __str__(self):
        sign = '+' if self.coef >= 0 else '-'
        coef_str = f'{sign}{str(abs(self.coef))}'
        x_str = exponent_to_variable_str('x', self.exp[0])
        y_str = exponent_to_variable_str('y', self.exp[1])
        parts = [coef_str, x_str, y_str]
        parts = [elem for elem in parts if elem != '']
        return '*'.join(parts)

    def weight(self, weights : list):
        if len(weights) != self.nvar:
            raise ValueError("Length mismatch between weights vector (%d) and \
                             number of variables (%d)" %(len(weights), self.nvar))
        return _dot_product(self.exp, weights)
    
    
class Polynomial:
    def __init__(self, monomials : list):
        if not isinstance(monomials, list):
            raise ValueError("Argument 'monomials' in Polynomial constructor must be a list")
        if not all([isinstance(monomial, Monomial) for monomial in monomials]):
            raise ValueError("Entries in monomials list 'monomials' in Polynomial constructor must be of type Monomial")
        
        # Monomials can appear with different number of variables
        # The number of variables of the polynomial is taken to be the maximum among the number of 
        # variables of its monomials
        # If a monomial has m variables and the polynomial has n variables, the monomial variables 
        # are assumed to be the first m variables
        self.monomials = monomials
        self.nvar = max([monomial.nvar for monomial in self.monomials])

    def weight(self, weights : list):
        if len(weights) != self.nvar:
            raise ValueError("Length mismatch between weights vector (%d) and \
                             number of variables (%d)" %(len(weights), self.nvar))
        weight_list = [monomial.weight(weights[:len(monomial)]) for monomial in self.monomials]
        return weight_list
    
    def weight_range(self, weights):
        weight_list = self.weight(weights)
        low = min(weight_list)
        high = max(weight_list)
        return low, high
    
    def _is_monomial(self):
        return len(self.monomials) == 1