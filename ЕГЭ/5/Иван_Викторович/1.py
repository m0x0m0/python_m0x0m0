res = []
for n in range(1, 1001):
    s = bin(n)[2:]
    if n % 3 == 0: s += s[-2:]
    else: s += bin(n % 3 * 3)[2:]
    if int(s, 2) >= 195:
        res.append(int(s, 2))
print(min(res))
