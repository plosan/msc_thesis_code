import os
import pandas as pd

def is_monomial_ideal(ideal_gen_str):
    for symbol in ('+', '-'):
        if symbol in ideal_gen_str:
            return False
    return True

# def parse_r_chain_file(filepath):


def str_to_bool(bool_str):
    if 'true' in bool_str:
        return True
    return False

def get_monomials(poly_str):
    mod_str = poly_str.replace('_', '')
    mod_str = mod_str.replace('-', '+')
    mon_list = mod_str.split('+')
    return mon_list

def get_binomial_exponents(poly_str):
    mon_list = get_monomials(poly_str)
    mon_list = [mon for mon in mon_list if not ('x' in mon and 'y' in mon)]
    # Monomials with only x 
    mon_x = [mon for mon in mon_list if ('x' in mon and 'y' not in mon)]
    exp_x = [int(mon.replace('x', '')) for mon in mon_x]
    # Monomials with only y 
    mon_y = [mon for mon in mon_list if ('x' not in mon and 'y' in mon)]
    exp_y = [int(mon.replace('y', '')) for mon in mon_y]
    # Return max exponents of x and y
    return max(exp_x), max(exp_y)

def macaulay2_output_to_csv(filepath, output_directory):

    df = pd.DataFrame(columns = ['char', 'cong', 'irred', 'nu-invariants', 'ideals'])
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if 'p = ' in line:
                # Parse characteristic and irreducibility line
                char_str, irred_str = line.split(',')
                char_str = char_str.split('=')[1].strip()
                p = int(char_str)
                is_irred = str_to_bool(irred_str)
                # Compute congruence mod ab
                poly_str = os.path.splitext(os.path.split(filepath)[-1])[0]
                a, b = get_binomial_exponents(poly_str)
                cong = p % (a * b)
                cong_neg = cong - (a * b)
                if abs(cong_neg) < cong:
                    cong = cong_neg 
                # Parse nu-invariants line
                nu_inv_str = next(file).strip()
                nu_inv_str = nu_inv_str.split('=')[1].strip()
                nu_inv_str = nu_inv_str[1:-1]
                # Parse ideals lines
                ideals = []
                ideal_line = next(file).strip()
                while ideal_line != '':
                    ideal_str = ideal_line.split(':')[1].strip()
                    ideals.append(ideal_str)
                    ideal_line = next(file).strip()
                ideals_str = ', '.join(ideals)
                # Append info to DataFrame
                df.loc[len(df)] = [p, cong, is_irred, nu_inv_str, ideals_str]

    # 
    fileroot = os.path.splitext(filename)[0]
    out_filename = f'{fileroot}.csv'
    out_fileroot = os.path.join(output_directory, out_filename)
    df.to_csv(out_fileroot, index = False)


if __name__ == "__main__":

    contents = os.listdir('../data')

    comp_type_list = [
        # 'binomial_deformation_e_chain',
        # 'binomial_deformation_e_chain_level',
        'binomial_deformation_r_chain',
        # 'binomial_deformation_r_chain_nu_invariants',
        # 'binomial_e_chain',
        # 'binomial_e_chain_level',
        'binomial_r_chain',
        # 'binomial_r_chain_nu_invariants',
    ]

    for comp_type in comp_type_list:

        print(f"Running {comp_type}")

        dir_path = os.path.join('..', 'data', comp_type)
        contents = os.listdir(dir_path)
        if 'dummy.txt' in contents:
            contents.remove('dummy.txt')
        contents.sort()

        out_path = os.path.join('..', 'dataframes', comp_type)
        if not os.path.exists(out_path):
            os.mkdir(out_path)
        for filename in contents:
            filepath = os.path.join(dir_path, filename)
            print(f'Processing {os.path.splitext(filepath)[0]}...')
            macaulay2_output_to_csv(filepath, out_path)
        