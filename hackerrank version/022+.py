def namescore(arg):
    score = 0
    letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    for i in arg:
        if i in letters:
            score += letters.index(i) + 1
    return score


namelist = []
t = int(input().strip())
for x in range(t):
    namelist.append(input().strip())
namelist.sort()

t = int(input().strip())
for x in range(t):
    i = input().strip()
    print(namescore(i) * (namelist.index(i) + 1))
