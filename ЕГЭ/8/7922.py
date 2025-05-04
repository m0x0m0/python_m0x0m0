from itertools import product

k=0
f = True
for w in product('авнрья', repeat=5):
    k += 1
    word = ''.join(w)
    if word[0] != 'я' and word.count('ь') < 2:
        if not((word[1] == 'я' and word[2] == 'я') or (word[2] == 'я' and word[3] == 'я') or (word[3] == 'я' and word[4] == 'я')):
            print(k, word)
#6406


