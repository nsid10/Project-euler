def palindrome(n):
    key = str(n)
    if key == key[::-1]:
        return True
    return False


t = int(input().strip())
for x in range(t):
    target = int(input().strip())
    sign = False
    for i in range((10**3 - 1)**2, (10**2)**2, -1):
        if palindrome(i):
            for k in range(10**3 - 1, 10**2, -1):
                if i % k == 0 and i / k >= 10**2 and i / k < 10**3:
                    sign = True
                    break
        if sign:
            break
    print(i)
