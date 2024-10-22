raz = set()
for i in range(2, 1000):
    s = i * '8'
    while '555' in s or '888' in s:
        s = s.replace('555', '8', 1)
        s = s.replace('888', '55', 1)
    raz.add(s)
print(len(raz))