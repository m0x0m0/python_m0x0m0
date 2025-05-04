def f(num):
    res = ''
    abc = '0123456789ab'
    while num > 0:
        res = str(abc[num%12]) + res
        num //= 12
    return res

maxi = 0
for n in range(143, 10000):
    r = f(n)
    if n % 12 == 0:
        r += r[-3:]
    else:
        r = f(3*(n % 12)) + r
    if int(r, 12) < 58000:
        if int(r, 12) > maxi:
            maxi = int(r, 12)
            print(maxi, n)
print(maxi)
#971