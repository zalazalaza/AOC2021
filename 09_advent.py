import numpy as np

def lowpoints(filename):
    data = np.pad((np.array([list(line.strip()) for line in (open(filename, 'r').readlines())])).astype(int), ((1,1),(1,1)), 'maximum')
    answer = 0
    bottoms  = []
    sizes = []
    
    for y in range(1,len(data)-1):
        for x in range(1,len(data[y])-1):
            lowest = min(data[y+1][x], data[y-1][x], data[y][x-1], data[y][x+1])
            if data[y][x] < lowest:
                answer += data[y][x]+1
                bottoms.append((y,x))
                
    for x in bottoms:
        h = find_bottom_left(data, x, [])
        sizes.append(len(h))
    
    sizes.sort(reverse = True)
    
    return (answer, np.prod(sizes[:3]))

def find_bottom_left(array, bottom, new_array):
    neighbors = [(bottom[0], bottom[1]-1), (bottom[0],  bottom[1]+1) , (bottom[0]+1, bottom[1]), (bottom[0]-1, bottom[1])]
    if bottom not in new_array:
        new_array.append(bottom)
    for i in neighbors:
        if array[i[0]][i[1]] < 9 and i not in new_array:
            new_array.append(i)
            find_bottom_left(array, i, new_array)
    return new_array
    
if __name__ == "__main__":
    print(lowpoints("9input.txt"))
