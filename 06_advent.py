import numpy as np


def lantern_fish(filename):
    starting_array = list(np.genfromtxt(filename, delimiter=",", dtype=int))
    count = [0,0,0,0,0,0,0,0,0]
    total = 0
    
    for i in starting_array:
        count[i] += 1

    for day in range(0,256):
        
        new_count = [count[1], count[2], count[3], count[4], count[5], count[6], count[7]+count[0], count[8], count[0]]
        count = new_count
    for x in count:
        total += x
    return total

if __name__ == "__main__":
    print(lantern_fish("6input.txt"))
