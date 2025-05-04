def div(n):
    d = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d.add(i)
            d.add(n//i)
    return sorted(d)

for x in range(700_001, 800_000):
    d = div(x)
    if len(d) >= 2:
        M = min(d) + max(d)
    else:
        M = 0
    if M % 10 == 4:
        print(x, M)
