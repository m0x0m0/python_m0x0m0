from itertools import *
abc = '012345678'
k = 0

for w in product(abc, repeat=5):
    n = ''.join(w)
    if n[0] != '0' and n.count('0') == 1:
        for i in range(5):
            if n[i] == '0' and i != 4:
                if int(n[i-1]) % 2 == 0 and int(n[i+1]) % 2 == 0:
                    k += 1
                    print(n)
            if n[i] == '0' and i == 4:
                if int(n[i-1]) % 2 == 0:
                    k += 1
                    print(n)
print(k)