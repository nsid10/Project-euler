b = 15
n = 21
while(n < 10**12):
    btemp = 3 * b + 2 * n - 2
    ntemp = 4 * b + 3 * n - 3
    b = btemp
    n = ntemp
print(b)
