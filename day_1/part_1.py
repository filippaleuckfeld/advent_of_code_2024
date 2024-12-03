
import numpy as np

vector1 = []
vector2 = []

with open("input", 'r') as file:
    for line in file:
        values = line.split()
        vector1.append(int(values[0]))
        vector2.append(int(values[1]))

vector1 = np.array(vector1)
vector2 = np.array(vector2)

vector1.sort()
vector2.sort()

abs_difference = np.abs(vector1 - vector2)

sum_abs_difference = np.sum(abs_difference)

print(sum_abs_difference)