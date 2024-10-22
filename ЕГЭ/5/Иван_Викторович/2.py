for n in range(1, 10000):
    s = bin(n)[2:]
    if n % 7 == 0: s += bin(7)[2:]
    else: s += '1'
    i = int(s, 2)
    if i % 5 == 0: s += bin(5)[2:]
    else: s += '1'

    if int(s, 2) > 500000:
        print(n)
        break