import numpy as np


def power(filename):
    data = np.loadtxt(filename, dtype=str)   
    holder = [0]*len(data[0])
    reversi = [0]*len(data[0])
    for i in data:
        for j in range(len(i)):
            if i[j] == "1":
                holder[j] += 1
            else: holder[j] -= 1
    for x in range(len(holder)):
        if holder[x] > 0:
            holder[x] = "1"
            reversi[x] = "0"
        else:
            holder[x] = "0"
            reversi[x] = "1"
    
    return int("".join(holder),2) * int("".join(reversi),2)

def find_ox(array, index):
    counter = 0
    new_array = []
    if len(array) == 1:
        return int("".join(array), 2)
    else:
        for i in array:
            if i[index] == "1":
                counter += 1
            else:
                counter -= 1
        if counter >= 0:
            for i in array:
                if i[index] == "1":
                    new_array.append(i)
        else:
            for i in array:
                if i[index] == "0":
                    new_array.append(i)

        return find_ox(new_array, index+1)

def find_co(array, index):
    counter = 0
    new_array = []
    if len(array) == 1:
        return int("".join(array), 2)
    else:
        for i in array:
            if i[index] == "1":
                counter += 1
            else:
                counter -= 1
        if counter < 0:
            for i in array:
                if i[index] == "1":
                    new_array.append(i)
        else:
            for i in array:
                if i[index] == "0":
                    new_array.append(i)

        return find_co(new_array, index+1)



if __name__ == "__main__":
    print(power("3input.txt"))
    print(find_ox(np.loadtxt("3input.txt", dtype=str), 0) * (find_co(np.loadtxt("3input.txt", dtype=str), 0)))
