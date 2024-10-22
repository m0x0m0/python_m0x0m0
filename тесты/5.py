from itertools import product
s = 0
for w in product('аоу', repeat=5):
    s += 1
    word = ''.join(w)
    if s == 240:
        print(word)
        break