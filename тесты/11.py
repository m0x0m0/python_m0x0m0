from itertools import product
words = product('балкон', repeat=3)
k = 0
for w in words:
    word = ''.join(w)
    if 'б' in word:
        k += 1
print(k)