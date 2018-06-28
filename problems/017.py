def cardinal(num):
    if num < 20:
        names = [
            "zero", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen",
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
        ]
        return names[num]
    if num < 100:
        if num % 10 == 0:
            tens = [
                "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
                "eighty", "ninety"
            ]
            return tens[int(num // 10) - 2]
        return cardinal((num // 10) * 10) + " " + cardinal(num % 10)
    if num < 1000:
        if num % 100 == 0:
            return cardinal(num // 100) + " hundred"
        return cardinal(num // 100) + " hundred and " + cardinal(num % 100)
    if num < 1000000:
        if num % 1000 == 0:
            return cardinal(num // 1000) + " thousand"
        return cardinal(num // 1000) + " thousand and " + cardinal(num % 1000)


letters = 0
for i in range(1, 1000 + 1):
    letters += len(cardinal(i)) - cardinal(i).count(" ")
print(letters)
