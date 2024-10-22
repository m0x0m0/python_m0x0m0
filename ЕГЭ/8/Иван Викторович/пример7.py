from itertools import product
s = []
for w in product('дкмо', repeat=5):
    word = ''.join(w)
    s.append(word)
print(s.index('комод') - s.index('домок') + 1)