n = int(input())
i = 0
while i < 10:
    i += 1
    if len(str(i**n)) == n:
        print(i**n)
