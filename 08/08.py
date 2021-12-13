import re
import numpy as np

def get_numbers(filename):
    starting_array = np.char.split(np.genfromtxt(filename, delimiter="|", dtype=str))
    nums = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdfge", "acf", "abcdefg", "abcdfg"]
    unique_lengths = [2, 3, 4, 7]
    final = 0

    for i in starting_array:
        answer =""
        unique_set = sorted(["".join(sorted(word)) for word in i[0] if len(word) in unique_lengths], key=len)
        zero_six_nine = ["".join(sorted(word)) for word in i[0] if len(word)==6]
        two_three_five = ["".join(sorted(word)) for word in i[0] if len(word)==5]
        unique_set.sort(key=len)
        search_chars = [unique_set[2][1], unique_set[2][3], unique_set[2][2]]
        nums = [0,unique_set[0], 0, 0, unique_set[2], 0,0, unique_set[1], unique_set[3], 0]
        
        for z in zero_six_nine:
            score = 0
            for x in nums[4]:
                if x in z:
                    score += 1
            for y in nums[1]:
                if y in z:
                    score += 1
            if score == 6:
                nums[9] = z
            elif score == 5:
                nums[0] = z
            else:
                nums[6] = z
        
        for z in two_three_five:
            score = 0
            for x in nums[1]:
                if x in z:
                    score += 1

            if score == 2:
                nums[3] = z
            else:
                score = 0
                for y in nums[9]:
                    if y in z:
                        score += 1
                if score == 5:
                    nums[5] = z
                else:
                    nums[2] = z
                    
        sorted_answers = ["".join(sorted(word)) for word in i[1]]
        for j in sorted_answers:
            for z in range(len(nums)):
                if j == nums[z]:
                    answer += str(z)
        final += int(answer)

    return final








if __name__=="__main__":
    print(get_numbers("08.txt"))
