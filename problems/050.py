def primality(n):
    if type(n) != int:
        raise TypeError("argument must be of type 'int'")
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5 + 1), 2):
        if n % x == 0:
            return False
    return True


target = 1000000
stream = []
i = 2
while sum(stream) < target:
    if primality(i):
        stream.append(i)
    i += 1
limit = len(stream)
flag = False
for i in range(limit):
    for j in range(i + 1):
        if sum(stream[i - j:limit - j]) < target:
            if primality(sum(stream[i - j:limit - j])):
                flag = True
                break
    if flag:
        break

print(sum(stream[i - j:limit - j]))
