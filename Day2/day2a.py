count = 0
line_count = 0

with open('input.txt', 'r') as file:
    for line in file:
        line_count += 1
        lvl = line.split()
        lvl = [int(x) for x in lvl]
        safe = True
        dir = None
        
        for i in range(len(lvl) - 1):
            diff = abs(lvl[i] - lvl[i + 1])
            if diff < 1 or diff > 3:
                safe = False
                break
            
            if dir is None:
                if lvl[i] < lvl[i + 1]:
                    dir = True
                elif lvl[i] > lvl[i + 1]:
                    dir = False
            else:
                if dir and lvl[i] >= lvl[i + 1] or not dir and lvl[i] <= lvl[i + 1]:
                    safe = False
                    break

        if safe:
            count += 1

print(count)
print(line_count)
