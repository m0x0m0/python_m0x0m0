res = []

for n in range(8**3, 8**4):
    s = str(n)
    s1 = int(s[0]) + int(s[-1])
    s2 = int(s[1]) + int(s[2])

    if s1 > s2: r = str(s2) + str(s1)
    else: r = str(s1) + str(s2)

    if int(r) == 317: res.append(n)
print(min(res) + max(res))
