from itertools import product
k = 0
for w in product('обществ', repeat=5):
    word = ''.join(w)
    if word[0] not in 'щб' and word[-2:] == 'вв' and 'ев' not in word \
            and 'ве' not in word and 'тб' in word:
        k += 1
print(k)