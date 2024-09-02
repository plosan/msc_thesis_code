import tools

if __name__ == "__main__":
    
    p = 5
    n = 17
    
    coefs = tools.p_adic_expansion(p=p, m=n)
    
    print(coefs)
    
    tools.p_adic_expansion_check(p, n, coefs)