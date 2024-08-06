import os
import pandas as pd

import math

def compare_binomial_to_deformation(bin_filepath, def_filepath):

    # Extract binomial exponents
    binomial = os.path.split(bin_filepath)[-1]
    binomial = os.path.splitext(binomial)[0]
    parts = binomial.split('_')
    exp_x = int(parts[0][1:])
    exp_y = int(parts[-1][1:])

    if math.gcd(exp_x, exp_y) != 1:
        print(exp_x, exp_y)
        return
    


    # Extract deformation
    deformation = os.path.split(def_file)[-1]
    deformation = os.path.splitext(deformation)[0]

    min_prime = exp_x * exp_y

    # Open binomial dataframe
    bin_df = pd.read_csv(bin_filepath)
    bin_df = bin_df[bin_df['char'] > min_prime]

    if bin_df.empty:
        print("Not enough data (bin)")
        return

    # Open deformation dataframe
    def_df = pd.read_csv(def_filepath)
    def_df = def_df[def_df['char'] > min_prime]
    if def_df.empty:
        print("Not enough data (bin)")
        return
    
    common_p = set(bin_df['char'].tolist()).intersection(set(def_df['char'].tolist()))
    common_p = list(common_p)
    common_p.sort()

    for p in common_p:
        if p % (exp_x * exp_y) != 1:
            continue
        # Extract rows of the characteristic
        bin_row = bin_df.loc[bin_df['char'] == p]
        def_row = def_df.loc[def_df['char'] == p]
        # Compare Frobenius roots
        # print(bin_row['ideals'])
        # print(def_row['ideals'])
        bin_ideals = bin_row['ideals'].to_string().split(',')
        def_ideals = def_row['ideals'].to_string().split(',')

        if bin_ideals != def_ideals:
            print(f'Different: p = {p}, bin = {binomial}, def = {deformation}')
            print(f'{bin_row["ideals"].to_string()}')
            print(f'{def_row["ideals"].to_string()}')

if __name__ == "__main__":
    pd.set_option('display.max_colwidth', None) 
    bin_dir = os.path.join('..', 'dataframes', 'binomial_r_chain')
    def_dir = os.path.join('..', 'dataframes', 'binomial_deformation_r_chain')

    bin_list = os.listdir(bin_dir)
    bin_list.sort()
    def_list = os.listdir(def_dir)


    for bin_file in bin_list:
        binomial = os.path.splitext(bin_file)[0]

        deformations = [def_file for def_file in def_list if binomial in def_file]
        for def_file in deformations:
            bin_filepath = os.path.join(bin_dir, bin_file)
            def_filepath = os.path.join(def_dir, def_file)
            compare_binomial_to_deformation(bin_filepath, def_filepath)
            # print(f'{binomial}', compare_binomial_to_deformation(binomial, ''))
