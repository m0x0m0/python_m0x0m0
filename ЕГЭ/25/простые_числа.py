def p(x):
    return x > 1 and all(x%i!= 0 for i in range(2, int(x**0.5) + 1))

for n in range(4_202_865, 4_202_923 + 1):
    if p(n):
        print(n)