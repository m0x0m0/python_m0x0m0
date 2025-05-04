from itertools import product
k = 0

for w in product('012345678', repeat=6):
    num = ''.join(w)
    if (num[0] != '0' and int(num[0])%2 == 0 and num[-1] != '2' and num[-1] != '3' and num.count('1') >= 2):
        k += 1
print(k)
#19868