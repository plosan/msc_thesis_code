import math
import tools
import pandas as pd
from matplotlib import pyplot as plt

def divides(mon1, mon2):
    exp_comp = [mon1[i] <= mon2[i] for i in range(len(mon1))]
    return all(exp_comp)

def dot_prod(v1, v2):
    return sum([v1[i] * v2[i] for i in range(len(v1))])

def count_monomials_dividing(p, a, b, r, mon_tgt):
    
    def_mon = tools.mu_const_def_monomials(a, b)
    alpha = [mon[0] for mon in def_mon]
    beta = [mon[1] for mon in def_mon]
    exponents = []
    basis_elem_list = []
    
    for t in range(r + 1):
        # Find out how many monomials of f^r divide the target monomial
        # when they are expressed in the standard basis
        exp_x = a * t
        exp_y = b * (r - t)
        floor_exp_x = int(math.floor(exp_x / p))
        floor_exp_y = int(math.floor(exp_y / p))
        mon_exp = (floor_exp_x, floor_exp_y)
        basis_exp_x = exp_x % p
        basis_exp_y = exp_y % p
        if divides(mon_exp, mon_tgt):
            exponents.append(t)
            basis_elem_list.append((basis_exp_x, basis_exp_y))
            
    # Find out how many monomials of H_r divide the target monomial
    # when they are expressed in the standard basis
    interaction_count = 0
    h_count = 0
    for s in range(r):
        k_tuple_list = tools.generate_monomials(4, r - s + 1)
        for k_tuple in k_tuple_list:
            alpha_sum = dot_prod(alpha, k_tuple)
            beta_sum = dot_prod(beta, k_tuple)
            for i in range(s + 1):
                exp_x = a * i + alpha_sum
                exp_y = b * (s - i) + beta_sum
                floor_exp_x = int(math.floor(exp_x / p))
                floor_exp_y = int(math.floor(exp_y / p))
                mon_exp = (floor_exp_x, floor_exp_y)
                if divides(mon_exp, mon_tgt):
                    h_count += 1
                
                basis_exp_x = exp_x % p
                basis_exp_y = exp_y % p

                basis_elem = (basis_exp_x, basis_exp_y)
                if basis_elem in basis_elem_list:
                    interaction_count += 1
    return exponents, interaction_count, h_count
    

if __name__ == "__main__":
    
    
    # x^5 + y^7 + x^5*y^2 + x^3*y^3 + x^4*y^3 + x^5*y^3
    
    a, b = 7, 5
    p = tools.find_primes_congruent(a*b, 1)[0]
    mon_tgt = (2, 2)
    mon_tgt_x, mon_tgt_y = mon_tgt
    
    # f_count = []
    # int_count_list = []
    # h_count_list = []
    
    # for r in range(p):
    #     r_exponents, interaction_count, h_count = count_monomials_dividing(p, a, b, r, mon_tgt)
    #     f_count.append(len(r_exponents))
    #     int_count_list.append(interaction_count)
    #     h_count_list.append(h_count)
    #     print("r = %2d, int_count = %5d, h_count = %d, " %(r, len(r_exponents), h_count))
    
    # try:
    #     nu_inv = f_count.index(0)
    # except ValueError:
    #     nu_inv = p - 1
        
    # print(nu_inv)
    
    # data_dict = {
    #     'r' : list(range(p)),
    #     'f_count' : f_count,
    #     'interaction_count' : int_count_list,
    #     'h_count' : h_count_list
    # }
    
    filename = f'interaction_count_x{a}_y{b}_mon_{str(mon_tgt)}.csv'
    # data = pd.DataFrame(data_dict)
    # data.to_csv(filename, index=False)
    
    data = pd.read_csv(filename)
    r_axis_list = data['r']
    f_count_list = data['f_count']
    int_count_list = data['interaction_count']
    h_count_list = data['h_count']
    
    plt.rcParams.update({
        "text.usetex": True,
        # "font.family": "Helvetica"
    })
    
    fig, ax = plt.subplots()
    ax.set_title(f"$f = x^{a} + y^{b}, p = {p}$")
    ax.plot(range(p), f_count_list, '-o', color='r', label=f"$\#$ coefficients of $F_\\ast^1 f^r$ that divide the monomial $x^{mon_tgt_x} y^{mon_tgt_y} \\in froot(f^r)$")
    ax.plot(range(p), int_count_list, '-o', color='b')
    ax.plot(range(p), h_count_list, '-o', color='g', label=f"$\#$ coefficients of $F_\\ast^1 H_r$, where $H_r = g^r - f^r$, that divide $x^{mon_tgt_x} y^{mon_tgt_y} \\in froot(f^r)$")
    ax.set_xlim([-0.5, p])
    ax.set_ylim([-0.5, 40])
    ax.set_xlabel("Exponent r")
    ax.set_aspect('equal')
    ax.legend(loc='upper left')
    ax.grid()
    plt.show()
    
    
    
        
    # mon_dividing = count_monomials_dividing(p, a, b, r, mon_tgt)
    # rs = [elem[0] for elem in mon_dividing]
    # print(rs)
    
    