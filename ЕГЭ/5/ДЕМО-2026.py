res = ''
l = []
for n in range(1, 13):
    res = bin(n)[2:]
    if n % 2 == 0:
        l.append(int('10' + res, 2))
    else:
        l.append(int('1' + res + '01', 2))
print(max(l))
