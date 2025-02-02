for n in range(1, 100):
    b = bin(n)[2:]
    if b.count('1') % 2 != 0:
        b = b + '1'
    else:
        b = b + '0'
    if b.count('1') % 2 != 0:
        b = b + '1'
    else:
        b = b + '0'
    if int(b, 2) > 75:
        break
print(int(b, 2))
