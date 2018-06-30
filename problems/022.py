def namescore(arg):
    score = 0
    letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    for i in arg:
        if i in letters:
            score += letters.index(i) + 1
    return score


names = open("/home/nahian/Documents/Python/p022_names.txt", "r")
namelist = names.read().split(',')
namelist.sort()
points = namescore(i) * (namelist.index(i) + 1)
print(points)
