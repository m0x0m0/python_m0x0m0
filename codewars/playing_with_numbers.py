def dig_pow(n, p):
    suma = 0
    for num in str(n):
        suma += int(num) ** p
        p += 1
    k = 1
    while k != 15000:
        if suma == n * k:
            return k
        elif k == 14999:
            return -1
        else:
            k += 1
print(dig_pow(int(input()), int(input())))
