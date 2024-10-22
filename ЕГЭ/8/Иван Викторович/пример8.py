from itertools import product
s = 0
for w in product('еклост', repeat=5):
    s += 1
    word = ''.join(w)
    if word[0] == 'c' and 'оо' in word:
        print(s)
        break