import math
import tools
import numpy as np

if __name__ == "__main__":
    
    N = 5
    a = 8
    p = tools.find_primes_congruent(a, -1)[0]

    
    d = 3
    q = p**d
    print(f'congruence = {q % a}')
    m = int(N * (q + 1) / a - 1)
    
    c0 = int(N * (p + 1) / a - 1)
    
    m1_c = (m - c0) / p
    m1_t = N * (p**(d-1) - 1) / a
    
    print(f'm  = {m}')
    print(f'c0 = {c0}')
    print(f'cong = {m % p}')
    
    print(f'm1_c = {m1_c}')
    print(f'm1_t = {m1_t}')
    
    c1_c = m1_c - p * math.floor(m1_c / p)
    c1_t = p - N * (p + 1) / a
    
    print(f'c1_c = {c1_c}')
    print(f'c1_t = {c1_t}')
    
    quit()
    
    
    if N >= a:
        raise ValueError("Condition 0 <= N < a not satisfied")
    
    for p in primes:
        for d in range(0, 6):
            q = p**d
            m = N * q / a
            m_floor_c = np.floor(m)
            m_floor_t = 0
            if d % 2 == 0:
                m_floor_t = N * (q - 1) / a
            else:
                m_floor_t = N * (q + 1) / a - 1
            diff = m_floor_t - m_floor_c
            
            if diff != 0:
                print('%5d%5d%5s%d' %(p, d, '', diff))
                print('%d' %math.floor(math.log10(m_floor_c)))
                print('%d' %math.floor(math.log10(m_floor_t)))
                print('\n')