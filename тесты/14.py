from itertools import product
k = 0
for w in product('аборст', repeat=3):
    word = ''.join(w)
    if word.count('р') == 1:
        k += 1
print(k)