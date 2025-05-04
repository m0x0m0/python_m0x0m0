from itertools import *
k = 0
for i in product('тимашевск', repeat=5):
    s = ''.join(i)
    w = ''.join(i)
    s = s.replace('м', 'т').replace('в', 'т').replace('с', 'т').replace('к', 'т').replace('а', 'и').replace('е', 'и')
    if s.count('ш') + s.count('т') < s.count('и') and 'иш' not in s and 'ши' not in s:
        k += 1
        print(w)
print(k)
