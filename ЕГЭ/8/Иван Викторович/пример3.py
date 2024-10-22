from itertools import product
k = set()
for w in product('размах', repeat=6):
    word = ''.join(w)
    if word.count('р') + word.count('м') + word.count('з') + word.count('х') >= 3:
        k.add(word)
print(len(k))

#пример где нужно составить РАЗЛИЧНЫЕ последовательности
