def f(num):
    res = ''
    while num > 0:
        res = str(num%3) + res
        num //= 3
    return res

for n in range(1, 100):
    r = f(n)
    if n % 3 != 0:
        suma = sum([int(el) for el in r])
        r = r + f(suma)
    else:
        r = r + r[-2:]
    if (int(r, 3) % 2 == 0) and (int(r, 3) > 220):
        print(int(r, 3))
#222

