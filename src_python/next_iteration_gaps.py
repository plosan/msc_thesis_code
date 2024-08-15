
def parse_nu_invariants_str(nu_inv_str):
    nu_inv_list = nu_inv_str.replace(',', '').split(' ')
    nu_inv_list = [int(nu_inv) for nu_inv in nu_inv_list]
    return nu_inv_list




if __name__ == "__main__":


    nu_inv_str = '19, 27, 30, 32, 36, 39, 42, 43, 48, 51, 54, 56, 57, 60, 63, 65, 68, 69, 72, 75, 76, 80, 81, 84, 87, 90, 92, 93, 96, 98, 101, 102, 105, 108, 109, 111, 113, 114, 116, 117, 120'

    nu_inv_list = parse_nu_invariants_str(nu_inv_str)
    print(nu_inv_list)
    nu_inv_list.insert(0, 0)
    print(nu_inv_list)

    p = 11
    e = 2
    pe = p ** e


    known_exponents = []
    for i in range(len(nu_inv_list) - 1):
        low = nu_inv_list[i] + 1
        high = nu_inv_list[i + 1]
        known_interval = list(range(p * low, p * high + 1))
        known_exponents += known_interval

    all_exponents = list(range(p ** (e + 1)))

    unknown_exponents = set(all_exponents).difference(set(known_exponents))
    unknown_exponents = list(unknown_exponents)
    unknown_exponents.sort()

    intervals = []

    prev_low = 0
    for i in range(len(unknown_exponents) - 1):
        if unknown_exponents[i + 1] - unknown_exponents[i] > 1:
            high = unknown_exponents[i]
            intervals.append((prev_low, high))
            prev_low = unknown_exponents[i + 1]

    for interval in intervals:
        print(interval)

    