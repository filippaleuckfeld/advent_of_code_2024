vector1 = []
vector2 = []

with open("input", 'r') as file:
    for line in file:
        values = line.split()
        vector1.append(int(values[0]))
        vector2.append(int(values[1]))

similarity_dict = {}

for value in vector1:
    if value in similarity_dict:
        similarity_dict[value][0] += 1
    else:
        similarity_dict[value] = [1, 0]

for value in vector2:
    if value in similarity_dict:
        similarity_dict[value][1] += 1
    else:
        similarity_dict[value] = [0, 1]

total_sum = 0
for value, (x, y) in similarity_dict.items():
    total_sum += x * y * value

print(total_sum)