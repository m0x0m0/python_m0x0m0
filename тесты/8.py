from itertools import product
k = 0
for w in product('пирог', repeat=4):
    word = ''.join(w)
    if (word.count('о') == 1 and ('ро' in word or 'по' in word or 'го' in word)) \
            or word.count('о') == 0 \
            or word.count('о') == 2 and word[1] == 'о' and word[3] == 'о' and word[0] in 'прг' and word[2] in 'прг':
        k += 1
print(k)