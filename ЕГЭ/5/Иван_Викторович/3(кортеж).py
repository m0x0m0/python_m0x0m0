def f(d):
    lst = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    while d > 0:
        result = lst[d % 12] + result
        d //= 12
    return result

res = []

for n in range(144, 1000):
    s = f(n)
    if n % 12 == 0: s += s[-3:]
    else: s = f(n % 12 * 3) + s
    if int(s, 12) < 58000:
        res.append((int(s, 12), n))
print(sorted(res, reverse=True)[0])