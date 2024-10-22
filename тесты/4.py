from itertools import product
s = 0
for w in product('клрт', repeat=4):
    s += 1
    word = ''.join(w)
    if s == 67:
        print(word)
        break