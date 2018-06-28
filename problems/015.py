from math import factorial as fact

m, n = 20, 20
print(fact(m + n) // (fact(m) * fact(n)))
