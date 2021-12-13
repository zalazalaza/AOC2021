import numpy as np

regexp = r"(\d+)"
output = np.fromregex("5input.txt", regexp, [('num1', float), ('num2', float)])
print(output)
