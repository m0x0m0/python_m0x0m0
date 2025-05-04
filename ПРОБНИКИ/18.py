f = open('18.txt')
l = []
res = []

for s in f:
    s = s.replace(',', '.')
    l.append(float(s))


max_suma = l[0]
for i in range(498):
    if abs(l[i]-l[i+1]) <= 10:
        max_suma += l[i+1]
    else:
        res.append(max_suma)
        max_suma = l[i+1]

print(max(res))
