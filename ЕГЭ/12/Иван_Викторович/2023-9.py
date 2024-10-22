def simple(suma):
    for a in range(2, round(suma**0.5) + 1):
        if suma % a == 0:
            return False
    return True


for n in range(1, 1000):
    s = '9' + n * '1' + n * '2'
    while '91' in s or '92' in s:
        if '91' in s:
            s = s.replace('91', '39', 1)
        if '92' in s:
            s = s.replace('92', '59', 1)
    summa = sum([int(i) for i in s])
    if simple(summa) and summa in range(100, 1000):
        print(n)
        break

