def base(i, b):
    new = ''
    while i >= b:
        new += str(i % b)
        i = i // b
    new += str(i)
    return new[::-1]


def palindrome(n):
    key = str(n)
    if key == key[::-1]:
        return True
    return False


n, k = input().split(' ')
n, k = [int(n), int(k)]

sum = 0
for i in range(n):
    if palindrome(i):
        if palindrome(base(i, k)):
            sum += i
print(sum)
