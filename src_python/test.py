import pandas as pd

from matplotlib import pyplot as plt

def _nu_inv_str_to_list(nu_inv_str):
    nu_inv_list = nu_inv_str.split(',')
    nu_inv_list = [int(elem.strip()) for elem in nu_inv_list]
    return nu_inv_list

if __name__ == "__main__":

    filepath = 'test.csv'

    df = pd.read_csv(filepath)

    primes = []
    data = []

    for _, row in df.iterrows():
        p = int(row['p'])
        nu_inv_list = _nu_inv_str_to_list(row['nu_inv'])
        data_elem = [nu_inv / p for nu_inv in nu_inv_list]
        data.append(data_elem)
        primes.append(p)

    fig, ax = plt.subplots()
    for i in range(len(data)):
        data_elem = data[i]
        x_axis = list(range(1, len(data_elem) + 1))
        ax.plot(x_axis, data_elem, marker = 'o', label = f'p = {primes[i]}')
    ax.legend()
    plt.show()