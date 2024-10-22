from itertools import product
s = []
for w in product('аоу', repeat=5):
    word = ''.join(w)
    s.append(word)
print(s.index('уауау') - s.index('оуоуа') + 1)