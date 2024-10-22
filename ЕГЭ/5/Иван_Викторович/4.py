res = []
for n in range(10000, 100000):
    s = oct(n)[2:]
    for _ in range(2):
        for c in '1357': s = s.replace(c, '2')
        s += str(n % 8)
    if int(s, 8) % 2023 == 0:
        res.append(n)
print(sum(res))