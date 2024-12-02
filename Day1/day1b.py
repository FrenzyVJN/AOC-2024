left_list = []
right_list = []
similarity_score = 0
with open('input.txt', 'r') as file:
    for line in file:
        line = line.split()
        left, right = int(line[0]), int(line[1])
        left_list.append(left)
        right_list.append(right)

for number in left_list:
    count = right_list.count(number)
    similarity_score += number * count
print(similarity_score)