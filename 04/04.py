import numpy as np

def mark_cards(number, cards):
    for i in cards:
        for j in i:
            j[j == number] = "X"
    return cards

def check_cards(file1, file2):
    call_numbers = np.loadtxt(file2, dtype=str, delimiter=",")
    pre_cards = np.loadtxt(file1, dtype=str)
    cards = np.split(pre_cards, pre_cards.shape[0]/5)
    
    for i in call_numbers:
        mark_cards(i, cards)
        for array in cards:
            for j in range(array.shape[0]):
                column = array[j]
                row = array[:, j]
                if np.all(row == "X") or np.all(column == "X"):
                    return (array, i) 

def reverse_check_cards(file1, file2):
    call_numbers = np.loadtxt(file2, dtype=str, delimiter=",")
    pre_cards = np.loadtxt(file1, dtype=str)
    cards = np.split(pre_cards, pre_cards.shape[0]/5)
    count = len(cards)

    for i in call_numbers:
        mark_cards(i, cards)
        for array in cards:
            for j in range(array.shape[0]):
                column = array[j]
                row = array[:, j]
                if (np.all(row == "X") or np.all(column == "X")) and array[0][0] != "W" and count > 1:
                    array[0][0] = "W"
                    count -= 1
                elif (np.all(row == "X") or np.all(column == "X")) and array[0][0] != "W" and count == 1:
                    return (array, i)
            

def count_total(array_tuple):
    winning_number = array_tuple[1]
    score = 0
    for i in array_tuple[0]:
        for j in i:
            if j != "X":
                score += int(j)
    return score*int(winning_number)

if __name__ == "__main__":
    print(count_total(reverse_check_cards("04.txt", "04_random.txt")))
    print(count_total(check_cards("04.txt", "04_random.txt")))
 
