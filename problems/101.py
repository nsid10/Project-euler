fx = [1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10 for n in range(1, 11)]
FITBOP = 0
while fx != []:
    FITBOP += sum(fx)
    fx = [fx[j + 1] - fx[j] for j in range(len(fx) - 1)]
print(FITBOP)
