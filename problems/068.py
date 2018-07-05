inner = [5, 4, 3, 2, 1]
outer = [6, 10, 9, 8, 7]
text = ''
n = inner[0]
for k in outer:
    flag = False
    for o in inner:
        if k + n + o == 14:
            text += str(k) + str(n) + str(o)
            n = o
            break
print(text)
