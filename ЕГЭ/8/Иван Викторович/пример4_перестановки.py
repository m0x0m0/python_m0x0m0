from itertools import permutations
k = set()
for w in permutations('ареал'):
    print(w)
    word = ''.join(w)
    if 'аа' not in word and 'ае' not in word and 'еа' not in word:
        k.add(word)
print(len(k))
