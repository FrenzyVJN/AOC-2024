left_list = []
right_list = []

with open('input.txt', 'r') as file:
    for line in file:
        line = line.split()
        left, right = int(line[0]), int(line[1])
        left_list.append(left)
        right_list.append(right)
    l = sorted(left_list)
    r = sorted(right_list)
    
    total_distance = 0
    
    for left, right in zip(l, r):
        distance = abs(left - right)
        total_distance += distance

print(total_distance)

