from math import factorial as fact

t = int(input().strip())
for x in range(t):
    pos = int(input().strip())
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    box = ''
    while len(letters) > 0:
        size = fact(len(letters)) // len(letters)
        box += letters[(pos - 1) // size]
        letters.pop((pos - 1) // size)
        while pos >= size:
            pos -= size
    print(box)
