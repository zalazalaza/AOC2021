import numpy as np

def insertion(filename):
    data = {x[0]:x[1] for x in (list(np.genfromtxt(filename, str, delimiter=" -> ")))}
    scores = {x:0 for x in data}
    sequence = "VHCKBFOVCHHKOHBPNCKO"
    letter_score = {x:0 for x in np.unique(np.asarray(list(sequence)))}
    for x in range(0,40):
        my_dict = {x:0 for x in data}
        if x == 0:
            for j in range(len(sequence)):
                letter_score[sequence[j]] += 1
                if j < len(sequence)-1:
                    scores[sequence[j]+sequence[j+1]] += 1
        for letters in scores:
            my_dict[letters[0]+data[letters]] += scores[letters]
            my_dict[data[letters] + letters[1]] += scores[letters]
            if scores[letters] > 0 and data[letters] in letter_score:
                letter_score[data[letters]] += scores[letters]
            elif scores[letters] > 0 and data[letters] not in letter_score:
                letter_score[data[letters]] = 1
        scores = my_dict
    return letter_score[max(letter_score, key=letter_score.get)] - letter_score[min(letter_score, key=letter_score.get)]

if __name__ == "__main__":
    print(insertion("14.txt"))
