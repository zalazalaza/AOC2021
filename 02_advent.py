import numpy as np


def course(filename):
    data = np.loadtxt(filename, dtype=str)   
    forward = 0
    depth = 0 
    aim = 0
    for i in data:
        if i[0] == "forward":
            forward += int(i[1])
            depth += (int(i[1]) * aim)
        elif i[0] == "down":
            aim += int(i[1])
        else:
            aim -= int(i[1])

    return (forward, depth, forward*depth)

if __name__ == "__main__":
    print(course("2input.txt"))
