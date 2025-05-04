f = open('tct')
res = []
k = 0
for s in f:
    k += 1
    a = list(map(int, s.split()))
    l = []
    if len(set(a)) == 3:
        if (a.count(list(set(a))[0]) == 3 and a.count(list(set(a))[1])==3) or (a.count(list(set(a))[0])==3 and a.count(list(set(a))[2])==3) or (a.count(list(set(a))[1])==3 and a.count(list(set(a))[2])==3):
            if a.count(list(set(a))[0]) == 1:
                if (list(set(a))[1]*3 + list(set(a))[2]*3)/6 < list(set(a))[0]:
                    res.append(k)
            elif a.count(list(set(a))[1]) == 1:
                if (list(set(a))[0]*3 + list(set(a))[2]*3)/6 < list(set(a))[1]:
                    res.append(k)
            elif a.count(list(set(a))[2]) == 1:
                if (list(set(a))[1]*3 + list(set(a))[0]*3)/6 < list(set(a))[2]:
                    res.append(k)
print(max(res))
#БОЖЕ КАК Я УСТАЛА ПИСАТЬ ЭТОТ КОД
#17975


