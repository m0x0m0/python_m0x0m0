from itertools import permutations
k = set()
for w in permutations('аммиакат'):
    word = ''.join(w)
    res = word.replace('а', '1').replace('и', '1').replace('м', '2').replace('к', '2').replace('т', '2')
    for i in range(8):
        if int(res[i-1]) + int(res[i]) == 2 or int(res[i-1]) + int(res[i]) == 4:
            k.add(word)
print(len(k))


#способ Ивана Викторовича
from itertools import permutations
k = set()
for w in permutations('аммиакат'):
    word = ''.join(w)
    s = ''
    for c in word:
        if c in '':
            s += g
        else:
            s += s
    if 'gg' in s or 'ss' in s:
        k.add(word)
print(len(k))
