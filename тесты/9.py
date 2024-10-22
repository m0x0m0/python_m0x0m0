from itertools import product
k = set()
for w in product('абвгдэюя', repeat=5):
    word = ''.join(w)
    if word.count('э') + word.count('ю') + word.count('я') == 2 and word[-1] in 'эюя' and word[-2] in 'эюя':
        print(word)
        k.add(word)
print(len(k))
