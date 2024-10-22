n1 = int(input())
my_set1 = set(list(map(int, (input()).split())))
n2 = int(input())
my_set2 = set(list(map(int, (input()).split())))
if my_set2 == my_set1:
    print('YES')
else:
    print('NO')