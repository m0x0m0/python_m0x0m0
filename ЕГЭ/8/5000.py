from itertools import *

k = 0
for i in set(permutations('аббатиса')):
    s = ''.join(i)
    print(s)
    s = s.replace('т', 'б').replace('с', 'б').replace('и', 'а')
    if 'аа' not in s and 'бб' not in s:
        k += 1
print(k)

'''   
ибаб
ббиа
баби
биаб
абиб
иабб
ббаи
баиб
аибб
биба
абби
ибба
'''