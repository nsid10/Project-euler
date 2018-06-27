def palindrome(n):
    key = str(n)
    if key == key[::-1]:
        return True
    return False


t = int(input().strip())
for x in range(t):
    target = int(input().strip())
    dg = 3
    sign = False
    for i in range(target - 1, (10**(dg - 1))**2, -1):
        if palindrome(i):
            for k in range(10**dg - 1, 10**(dg - 1), -1):
                if i % k == 0 and i / k >= 10**(dg - 1) and i / k < 10**dg:
                    sign = True
                    break
        if sign:
            break
    print(i)
