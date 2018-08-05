def score(word): return sum(ord(c) - 64 for c in word)


def tri(t): return ((1 + 8 * t) ** 0.5 - 1) / 2 % 1 == 0


print(sum(tri(score(x[1:-1])) for x in open('p042_words.txt').read().split(',')))
