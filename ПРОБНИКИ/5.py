for n in range(1, 100):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = r + '0'
        r = '10' + r[2:]
    else:
        r = r + '1'
        r = '11' + r[2:]
    print(n, int(r, 2))
    # if int(r, 2) > 19:
    #     print(n, int(r, 2))
print(24*4)
