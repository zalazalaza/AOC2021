import numpy as np

def find_corrupt(filename):
    data = np.genfromtxt(filename, str)
    my_dict = {"(":")",
            "{":"}",
            "[":"]",
            "<":">"}
    score_dict = {")":3,
            "]":57,
            "}":1197,
            ">":25137}
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    corrupted = []
    found = []
    score = 0
    for word in data:
        expected = []
        for i in word:
            if i in openers:
                expected.append(i)
            elif i in closers and i == my_dict[expected[-1]]:
                expected.pop()
            elif i in closers and i != my_dict[expected[-1]]:
                corrupted.append(word)
                found.append(i)
                break
    for bar in found:
        score += score_dict[bar]
    return (corrupted,score)


def complete_unfinished(corrupt_array, filename):
    my_dict = {"(":")",
            "{":"}",
            "[":"]",
            "<":">"}
    score_dict = {")":1,
            "]":2,
            "}":3,
            ">":4}
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    scores = []
    data = [word for word in (np.genfromtxt(filename, str)) if word not in corrupt_array]
    for word in data:
        score = 0
        expected = []
        for i in word:
            if i in openers:
                expected.append(i)
            elif i in closers and i == my_dict[expected[-1]]:
                expected.pop()
        
        to_complete = [my_dict[x] for x in expected][::-1]
        
        for x in to_complete:
            score = (score*5)+score_dict[x]

        scores.append(score)
    scores.sort()
    return scores[int(len(scores)/2)]

if __name__ == "__main__":
    print(complete_unfinished(find_corrupt("10input.txt")[0], "10input.txt"))
