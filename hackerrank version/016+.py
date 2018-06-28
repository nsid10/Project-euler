t = int(input().strip())
for x in range(t):
    n = int(input().strip())
    num = str(2**n)
    digits = 0
    for i in num:
        digits += int(i)
    print(digits)
