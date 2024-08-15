import os
import pandas as pd

import algebra

TRIVIAL_IDEAL_STR = 'ideal 1'
TRIVIAL_IDEAL = '1'

def _parse_characteristic(line):
    index_equal = line.index('=')
    _line = line[index_equal + 1:]
    _line = _line.strip()
    return int(_line)

def _parse_irreducible(line):
    index_equal = line.index('=')
    _line = line[index_equal + 1:]
    _line = _line.strip()
    return 'true' == _line

def _parse_nu_invariants(line):
    index_equal = line.index('=')
    _line = line[index_equal + 1:]
    _line = _line.strip()
    _line = _line[1:-1]
    return _line

def _parse_frobenius_root(line):
    index_colon = line.index(':')
    _line = line[index_colon + 1:]
    _line = _line.strip()
    return _line

def output_rchain_to_dataframe(filepath):
    with open(filepath, 'r') as file:
        # Read polynomial
        polynomial = file.readline().strip()    
        # Parse file
        data = pd.DataFrame(columns = ['p', 'irred', 'nu_inv', 'froots'])
        for line in file:
            if not line.startswith('p = '):
                continue
            # Parse characteristic of the field
            characteristic = _parse_characteristic(line)
            # Parse irreducible
            is_irred = _parse_irreducible(next(file))
            # Parse nu_invariants
            nu_inv_str = _parse_nu_invariants(next(file))
            # Parse Frobenius roots
            line = next(file).strip()
            froots = []
            while line != '':
                froots.append(_parse_frobenius_root(line))
                line = next(file).strip()
            # Append data to dataframe
            data.loc[len(data)] = [characteristic, is_irred, nu_inv_str, froots]
    return data

def parse_generator(gen_str):
    # Split the generator into its monomials
    monomials_str = []
    prev = 0
    for i in range(len(gen_str)):
        if gen_str[i] == '+' or gen_str[i] == '-':
            monomials_str.append(gen_str[prev : i])
            prev = i
    monomials_str.append(gen_str[prev:])
    # Convert the string monomials to Monomials
    monomials = [algebra.str_to_monomial(elem) for elem in monomials_str]
    return monomials

def parse_ideal_gens(ideal_str):

    gens = ideal_str.strip()

    if gens == TRIVIAL_IDEAL_STR:
        return TRIVIAL_IDEAL
    
    gens = gens[len('ideal(') : -1]
    gens = gens.split(',')

    gens = [parse_generator(gen) for gen in gens]

    return gens


if __name__ == "__main__":

    ideal_str_list = []

    with open('input.txt', 'r') as file:
        for line in file:
            ideal_str = line.split(':')[1]
            ideal_str_list.append(ideal_str.strip())

    min_max_weights = []

    for ideal_str in ideal_str_list:
        if ideal_str == TRIVIAL_IDEAL_STR:
            print(TRIVIAL_IDEAL_STR)
            min_max_weights.append((0, 0))
        else:
            gens = parse_ideal_gens(ideal_str)
            gens = [elem[0] if len(elem) == 1 else elem for elem in gens]
            weights = [gen.weight([7, 6]) for gen in gens]
            min_max_weights.append((min(weights), max(weights)))
            for i in range(len(weights)):
                print(f'\t%10s%5s%d' %(str(gens[i]), '', weights[i]))
            print()

    print()
    for i, pair in enumerate(min_max_weights):
        print('%5d : %s' %(i, str(pair)))

    


