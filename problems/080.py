from decimal import *

ss = 0
getcontext().prec = 102
for ir in range(1, 100):
    num = Decimal(ir).sqrt()
    ss += sum(int(i) for i in str(num).replace(".", "")[:100]) if num % 1 != 0 else 0
print(ss)
