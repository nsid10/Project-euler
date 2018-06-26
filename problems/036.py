def palindrome(n):
    key = str(n)
    if key == key[::-1]:
        return True
    return False


sum = 0
for i in range(1000000):
    if palindrome(i):
        if palindrome(format(i, 'b')):
            sum += i
print(sum)
