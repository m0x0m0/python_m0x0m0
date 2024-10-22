def is_prime(a):
    if a % 2 == 0:
        return a == 2
    d = 3
    while d * d <= a and a % d != 0:
        d += 2
    return d * d > a

m = int(input())
n = int(input())
list1 = []
for i in range(m, n+1):
    if is_prime(i) == True:
        list1.append(i)

if len(list1) != 0:
    print(*list1, sep='\n')
else:
    print('Absent')