def div(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(d)

for x in range(500_001, 501_000):
    d = div(x)

    res = [el for el in d if el%10 == 8 and el != 8]
    if len(res) > 0:
        print(x, min(res))
