from itertools import product
s = 0
for w in product('аклош', repeat=5):
    s += 1
    word = ''.join(w)
    if word == 'школа':
        print(s)
        break