from decimal import *

n, p = int(input()), int(input())
ss = 0
getcontext().prec = p + 5
for ir in range(1, n + 1):
    num = Decimal(ir).sqrt()
    ss += sum(int(i) for i in str(num).replace(".", "")[:p]) if num % 1 != 0 else 0
print(ss)
