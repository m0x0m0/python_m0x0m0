from itertools import product
k = 0

l=[]
for w in product('косуф', repeat=5):
    k += 1
    word = ''.join(w)
    if word.count('ф') == 0 and word.count('у') == 2:
        l.append(k)
print(max(l))

#2313