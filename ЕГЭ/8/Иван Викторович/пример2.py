from itertools import product
k = 0
for w in product('моисей', repeat=4):
    word = ''.join(w)
    if word[0] != 'й' and (('о' in word) or ('и' in word) or ('е' in word)):
        k += 1
print(k)

