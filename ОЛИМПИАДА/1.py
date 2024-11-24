n = int(input())

if n == 1 or n == 2:
    print(1)

elif n % 2 != 0:
    print((n//2 + 1)**2)

elif n % 2 == 0:
    print((n//2)**2)
