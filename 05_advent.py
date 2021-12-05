import numpy as np

def create_grid(filename):
    map_dict = {}
    dimensions = (0,0)
    temp_array = [] # create dictionary to return
    data =np.delete((np.loadtxt(filename, dtype=str, delimiter= " ")),1 ,1) # strip extra characters from input
    for i in data:
        first = i[0].split(",")
        second = i[1].split(",")
        temp_array.append([(int(first[0]), int(first[1])), (int(second[0]), int(second[1]))])
    for i in temp_array:
        for j in i:
            if j[0] > dimensions[0]:
                dimensions = (j[0], dimensions[1])
            elif j[1] > dimensions[1]:
                dimensions = (dimensions[0], j[1])
    grid = np.zeros((dimensions[0]+1, dimensions[1]+1))
    data = np.array(temp_array)
    map_dict["map"] = grid
    map_dict["data"] = data
    return map_dict

def edit_map(dictionary):
    counter = 0
    counter_array = []
    for i,j in dictionary["data"]:
        if i[0] == j[0] or i[1] == j[1]:
            counter_array.append(counter)
            counter += 1
        else:
            counter += 1
    for i in counter_array:
        first_tuple = (dictionary["data"][i][0])
        second_tuple = (dictionary["data"][i][1]) 
        if first_tuple[0] == second_tuple[0]:
            top = max(int(first_tuple[1]), int(second_tuple[1]))
            bottom = min(int(first_tuple[1]), int(second_tuple[1]))
            for x in range(bottom, top+1):
                dictionary["map"][x, int(first_tuple[0])] += 1
        elif first_tuple[1] == second_tuple[1]:
            top = max(int(first_tuple[0]), int(second_tuple[0]))
            bottom = min(int(first_tuple[0]), int(second_tuple[0]))
            for z in range(bottom, top+1):
                dictionary["map"][int(first_tuple[1]), z] += 1
    
    return ((dictionary["map"] > 1).sum())
        
def diagonal_map(dictionary):
    for coords in dictionary["data"]:
        x_result = coords[0][0] == coords[1][0]
        y_result = coords[0][1] == coords [1][1]
        if x_result:
            bottom = min(coords[0][1], coords[1][1]) 
            top = max(coords[0][1], coords[1][1])
            for i in range(bottom, top+1):
                dictionary["map"][coords[0][0], i] += 1
        elif y_result:
            bottom = min(coords[0][0], coords[1][0])
            top = max(coords[0][0], coords[1][0])
            for i in range(bottom, top+1):
                dictionary["map"][i, coords[0][1]] += 1
        else:
            if coords[0][0] < coords[1][0]:
                start = coords[0]
                end = coords[1]
                duration = end[0] - start[0]
                if start[1] < end[1]:
                    for i in range(0, duration+1):
                        dictionary["map"][(start[0])+i, (start[1])+i] += 1
                else:
                    for i in range(0, duration+1):
                        dictionary["map"][(start[0])+i, (start[1])-i] += 1
            else:
                start = coords[1]
                end = coords[0]
                duration = end[0] - start[0]
                if start[1] < end[1]:
                    for i in range(0, duration+1):
                        dictionary["map"][(start[0])+i, (start[1])+i] += 1
                else:
                    for i in range(0, duration+1):
                        dictionary["map"][(start[0])+i, (start[1])-i] += 1
 



    return ((dictionary["map"] > 1).sum())

if __name__ == "__main__":
    print(edit_map(create_grid("5input.txt")))
    print(diagonal_map(create_grid("5input.txt")))

