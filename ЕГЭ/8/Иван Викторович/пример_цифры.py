from itertools import product
k = 0
for w in product('012345678', repeat=5):
    word = ''.join(w)
    if word[0] not in '01357' and word[-1] not in '18' and word.count('3') <= 1:
        k += 1
print(k)