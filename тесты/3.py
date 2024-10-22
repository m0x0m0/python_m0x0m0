from itertools import product
words = product('acgt', repeat=5)
k = 0
for w in words:
    word = ''.join(w)
    if word.count('a') == 2:
        k += 1
print(k)