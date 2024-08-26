

if __name__ == "__main__":

    filename = 'specialized_7_4_p29.txt'
    nu_inv_str = 'nu-inv'

    nu_inv = set()

    with open(filename, 'r') as file:

        for line in file:
            line = line.strip()
            if nu_inv_str in line:
                nu_inv.add(line)

    print(nu_inv)
