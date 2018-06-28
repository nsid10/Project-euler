def cardinal(num):
    if num < 20:
        names = [
            "Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]
        return names[num]
    if num < 100:
        if num % 10 == 0:
            tens = [
                "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy",
                "Eighty", "Ninety"
            ]
            return tens[int(num // 10) - 2]
        return cardinal((num // 10) * 10) + " " + cardinal(num % 10)
    if num < 1000:
        if num % 100 == 0:
            return cardinal(num // 100) + " Hundred"
        return cardinal(num // 100) + " Hundred " + cardinal(num % 100)
    if num < 10**6:
        if num % 1000 == 0:
            return cardinal(num // 1000) + " Thousand"
        return cardinal(num // 1000) + " Thousand " + cardinal(num % 1000)
    if num < 10**9:
        if num % 10**6 == 0:
            return cardinal(num // 10**6) + " Million"
        return cardinal(num // 10**6) + " Million " + cardinal(num % 10**6)
    if num < 10**12:
        if num % 10**9 == 0:
            return cardinal(num // 10**9) + " Billion"
        return cardinal(num // 10**9) + " Billion " + cardinal(num % 10**9)
    if num == 10**12:
        return "One Trillion"
    return "Out of range"


t = int(input().strip())
for x in range(t):
    n = int(input().strip())
    print(cardinal(n))
