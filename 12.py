import numpy as np

def next_route(edge_array, current_array, finished_array):
    test_array = finished_array.copy()
    next_array = []

    if current_array == []:
        for edge in list(edge_array):
            if "start" in edge:
                if edge[1] == "start":
                    edge = [edge[1], edge[0]]
                current_array.append(list(edge))
    for path in current_array:
        potentials = []
        next_start = path[-1]
        if next_start == "end":
            finished_array.append(path)
        for edge in edge_array:
            if next_start in edge and "start" not in edge and next_start != "end":
                potentials.append(list(edge))
        for next_tuple in potentials:
            for value in next_tuple:
                if value == next_start:
                    pass
                elif value in path and ord(value[0]) > 95 and path[0] != "double":
                    new_array = path.copy()
                    new_array.insert(0, "double")
                    new_array.append(value)
                    next_array.append(new_array)
                elif value in path and ord(value[0]) > 95 and path[0] == "double":
                    pass
                else:
                    new_array = path.copy()
                    new_array.append(value)
                    next_array.append(new_array)                   
    
    last_items = np.asarray([i[-1] for i in next_array])

    if test_array != [] and test_array ==  finished_array:
        return finished_array
    if np.all(last_items == "end"):
        for i in next_array:
            finished_array.append(i)
        return finished_array
    else:
        return next_route(edge_array,next_array, finished_array)

def find_path(filename):
    edges = list(np.genfromtxt(filename, str, delimiter="-"))
    my_array = next_route(edges, [], [])
    print(len(my_array))

if __name__ == "__main__":
    find_path("12.txt")
