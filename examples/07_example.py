import numpy as np

file = '../7input.txt'
df7 = np.loadtxt(file, delimiter=',')


def fuel_expanse_constant(positions): 
    opt_dist = np.median(positions)
    print(opt_dist)
    fuel = np.sum(np.abs(positions - opt_dist))
    return fuel

def fuel_expanse_linear(positions):
    opt_dist = np.floor(np.mean(positions))
    fuel = np.sum((np.abs(positions - opt_dist) ** 2 + np.abs(positions - 
                  opt_dist)) / 2)
    return fuel


print(f'Part 1: {fuel_expanse_constant(df7)}')
print(f'Part 2: {fuel_expanse_linear(df7)}')

