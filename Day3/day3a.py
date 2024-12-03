import re
sum = 0
with open("input.txt") as f:
    data = f.readlines()
    pattern = "mul\((-?\d+),(-?\d+)\)"
    for i in data:
        matches = re.findall(pattern, i)
        for match in matches:
            x, y = int(match[0]), int(match[1])
            sum += x * y
print(sum)