from math import factorial as fact

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
box = ''
pos = 10**6
while len(num) > 0:
    size = fact(len(num)) // len(num)
    box += num[(pos - 1) // size]
    num.pop((pos - 1) // size)
    while pos >= size:
        pos -= size
print(box)
