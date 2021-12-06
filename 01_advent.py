import numpy as np

def count(filename):
    x = 0
    data = np.genfromtxt(filename, dtype=np.int32)
    for i in range(len(data)-1):
        if data[i] < data[i+1]:
            x += 1
    return x

def count_threes(filename):
    x = 0
    data = np.genfromtxt(filename, dtype=np.int32)       
    for i in range(len(data)-3):
        if (data[i] + data[i+1] + data[i+2]) <  (data[i+1] + data[i+2]+ data[i+3]):
            x += 1
    return x
        

if __name__ ==  "__main__":
    print(count("1input.txt"))
    print(count_threes("1input.txt"))
