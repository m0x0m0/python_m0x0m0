a, n = float(input()), int(input())
p, s = 1, 1
for i in range(1, n+1):
    p *= a
    s += p
print(int(s))