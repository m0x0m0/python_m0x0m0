def p(x):
    return x > 1 and all(x%i!=0 for i in range(2, int(x**0.5) + 1))

def div(x):
    d = set()
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x//i)
    return sorted(d)

for n in range(650_000, 660_000):
    res = [el for el in div(n) if p(el)]
    if len(res) > 0:
        s = sum(res)
        if s % 100 == 25:
            print(n, s)