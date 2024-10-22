from itertools import product
words = product('слон', repeat=5)
k = 0
for w in words:
    word = ''.join(w)
    if word.count('с') == 1:
        k += 1
print(k)