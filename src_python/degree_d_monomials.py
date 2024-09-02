import copy

import tools

if __name__ == "__main__":
    
    a = 7
    b = 5
    p = tools.find_primes_congruent(a*b, 1)[0]
    
    print(p)
    def_mon = tools.mu_const_def_monomials(a, b)
    print(def_mon)
    
    line = (b, a, a * b)
    def_mon_vals = [tools.line_func(line, mon) for mon in def_mon]
        
    
    for deg in range(1, p):
        n = len(def_mon)
        mon_list = tools.generate_monomials(n, deg)
        
        bad_monomials = []
        
        for mon in mon_list:
            sum = 0
            for k in range(n):
                sum += def_mon_vals[k] * mon[k]
            if sum % p == 0:
                bad_monomials.append(mon)
                
        if bad_monomials:
            print(f'deg = {deg}, count = {len(bad_monomials)}')
    
    # n = len(def_mon)
    
    # deg = -1
    
    # mon_list = tools.generate_monomials(n, deg)
    