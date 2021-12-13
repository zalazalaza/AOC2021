import numpy as np


def get_frequency(filename):
    starting_array = list(np.genfromtxt(filename, delimiter=",", dtype=int))
    answer = 9999999999999999999
    for i in range(0, max(starting_array)):
        result = 0
        for j in starting_array:
            if result < answer:
                result += abs(i-j)
            else:
                break
        if result < answer:
            answer = result
    return answer

def get_complex_frequency(filename):
    starting_array = list(np.genfromtxt(filename, delimiter=",", dtype=int))
    answer = 9999999999999999999
    for i in range(0, max(starting_array)):
        result = 0
        for j in starting_array:
            if result < answer:
                distance = abs(i-j)
                total = 0 
                for x in range(0, distance+1):
                    total = total + x
                result += total 
            else:
                break
        if result < answer:
            answer = result
    return answer



if __name__ == "__main__":
    print(get_complex_frequency("07.txt"))
