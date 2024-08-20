from matplotlib import pyplot as plt
import copy

VAR_TO_INDEX = {
    'x' : 0,
    'y' : 1
}

def get_gen_exponents(gen):
    
    var_str = gen.split('*')
    
    exps = [0, 0]
    
    for elem in var_str:
        parts = elem.split('^')
        if len(parts) == 1:
            var = parts[0]
            exps[VAR_TO_INDEX[var]] = 1
        else:
            var = parts[0]
            exp = int(parts[1])
            exps[VAR_TO_INDEX[var]] = exp
    return tuple(exps)

def extract_exponents(gen_str):
    
    gen_str = gen_str.replace('(', '')
    gen_str = gen_str.replace(')', '')
    gens = gen_str.split(',')
    
    exps = [get_gen_exponents(gen) for gen in gens]
    return exps

def remove_characters(elem_str, substr_list):
    out = copy.deepcopy(elem_str)
    for substr in substr_list:
        out = out.replace(substr, '')
    return out

def minimal_generating_system(gen_str):
    
    gen_str = remove_characters(gen_str, ['(', ')'])    
    exps = extract_exponents(gen_str)
    exps.sort()
    
    print(exps)
    
    min_gen_system = [exps[0]]
    
    for i in range(1, len(exps)):
        prev_y = exps[i-1][1]
        curr_y = exps[i][1]
        if curr_y < prev_y:
            min_gen_system.append(exps[i])
    
    print(min_gen_system)
    
    return min_gen_system


if __name__ == "__main__":
    
    a = 5
    b = 7
    
    # gen_str = '(x^3,x*y^3,x^2*y^2,y^5)'
    # gen_str_def = '(x^3,x*y^3,x^2*y^2,y^5,x*y^4,x^2*y^3)'
    gen_str = '(x*y^3,x^2*y^2,x^3*y,x^4,y^5)'
    gen_str_def = '(x*y^3,x^2*y^2,x^3*y,x^4,y^5,x*y^4)'
    
    min_gen_system = minimal_generating_system(gen_str)
    x_exps = [exp[0] for exp in min_gen_system]
    y_exps = [exp[1] for exp in min_gen_system]
    
    min_gen_system_def = minimal_generating_system(gen_str_def)
    x_exps_def = [exp[0] for exp in min_gen_system_def]
    y_exps_def = [exp[1] for exp in min_gen_system_def]
    
    axis_lim = max(x_exps + y_exps + x_exps_def + y_exps_def)
    
    fig, ax = plt.subplots()
    ax.plot(x_exps, y_exps, '-bo', label='pol')
    ax.plot(x_exps_def, y_exps_def, '-ro', label='def')
    ax.axhline(y = 0, color='k', lw=1)
    ax.axvline(x = 0, color='k', lw=1)
    ax.set_xlim([-0.5, axis_lim + 1])
    ax.set_ylim([-0.5, axis_lim + 1])
    ax.legend(loc='upper right')
    ax.set_aspect('equal')
    plt.show()