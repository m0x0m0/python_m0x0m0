from itertools import product
s = 0
for w in product('агилморт', repeat=4):
    s += 1
    word = ''.join(w)
    if word == 'гоаа':
        print(s)
        break