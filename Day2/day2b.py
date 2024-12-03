def is_safe(lvl):
        dir = None
        for i in range(len(lvl) - 1):
            diff = abs(lvl[i] - lvl[i + 1])
            if diff < 1 or diff > 3:
                return False
            
            if dir is None:
                if lvl[i] < lvl[i + 1]:
                    dir = True
                elif lvl[i] > lvl[i + 1]:
                    dir = False
            else:
                if dir and lvl[i] >= lvl[i + 1]:
                    return False

                elif not dir and lvl[i] <= lvl[i + 1]:
                    return False
        return True
count = 0
with open("input.txt", 'r') as file:
    for line in file:
        lvl = line.split()
        lvl = [int(x) for x in lvl]            
        # print(lvl) BRUH
        for i in range(len(lvl)):
            mod_lvl = lvl[:i] + lvl[i+1:]
            if is_safe(mod_lvl):
                count += 1
                break
            
print(count)