n = int(input())
if n < 10:
    print(1)
elif str(n)[-1] in '1234':
    print(n//5 + 1)
else:
    print(n//5)