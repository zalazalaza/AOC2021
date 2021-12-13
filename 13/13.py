import numpy as np

def fold(filename, foldname):
    points = np.genfromtxt(filename, int, delimiter=",")
    folds = np.loadtxt(foldname, str, delimiter="=")
    for fold in folds:
        line = int(fold[1])
        if fold[0] == "x":
            for i in range(len(points)):
                if points[i][0] > line:
                    points[i] = [line - (points[i][0]-line), points[i][1]]
        elif fold[0] == "y":
            for i in range(len(points)):
                if points[i][1] > line:
                    points[i] = [points[i][0], line - (points[i][1]-line)]
    return np.unique(points, axis=0)

def print_letters(coordinates):
    words = open("13words.txt", 'w')
    highest = 0
    for coord in coordinates:
        if coord[0] > highest:
            highest = coord[0]
        elif coord[1] > highest:
            highest = coord[1]
    letter_grid = np.full((highest*2,highest*2),".", dtype=str)
    for i in coordinates:
        letter_grid[i[1]][i[0]] = "#"
    for i in letter_grid:
        line = "".join(i) + "\n"
        words.write(line)


if __name__ == "__main__":
    letters = fold("13.txt", "13fold.txt")
    print_letters(letters)
