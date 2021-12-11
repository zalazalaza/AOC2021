import numpy as np
import copy

def flash(grid):
    if np.any(grid > 9):
        for y in range(1, len(grid)-1):
            for x in range(1, len(grid[y])-1):
                if grid[y][x] > 9:
                    my_slice = grid[y-1:y+2,x-1:x+2] 
                    my_slice = my_slice + 1
                    my_slice[my_slice == 1] = 0
                    grid[y-1:y+2,x-1:x+2] = my_slice
                    grid[y][x] = 0
                    grid[grid < 0] = -9
        return flash(grid)
    else:
        return grid


def octo_flash(filename):
    data = np.pad(np.array([list(line.strip()) for line in (open(filename, 'r').readlines())]).astype(int), ((1,1),(1,1)),constant_values=-8)
    score = 0
    for cycle in range(0, 500):
        data = data + 1
        data = flash(data)
        score += np.sum(data == 0)
        my_grid = data[1:-1,1:-1]
        if np.all(my_grid == my_grid[0][0]):
            print(cycle+1)
            break
    print(score)

if __name__ == "__main__":
    octo_flash("11input.txt")
   
