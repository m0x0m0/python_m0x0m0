cnt = 0
f = open('txt.1')
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    print(a)
    if (min(a) + max(a))**2 > a[1]**2 + a[2]**2 + a[3]**2:
        cnt+=1
print(cnt)