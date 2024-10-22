from itertools import product
k = 0
for w in product('абвгде', repeat=4):
    word = ''.join(w)
    if word.count('г') == 1 and (word[0] == 'г' or word[-1] == 'г'):
        k += 1
print(k)