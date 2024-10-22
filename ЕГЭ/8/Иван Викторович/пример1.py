from itertools import product
words = product('весна', repeat=3)
k = 0
for w in words:
    word = ''.join(w)
    if 'а' in word:
        k += 1
print(k)