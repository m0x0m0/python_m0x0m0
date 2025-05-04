f = open('17.txt').readlines()

l = []
for el in f:
    if el.isdigit() == 0:
        l.append(int(el[:-1]))
    else:
        l.append(int(el))
k = 0
maxi = 0
for i in range(1, len(l)):
    if l[i-1] % 16 == min(l) or l[i] % 16 == min(l):
        k += 1
        if (l[i-1] + l[i]) > maxi:
            maxi = l[i-1] + l[i]
    if l[i] == 73279:
        print('da)')
print(k, maxi)

