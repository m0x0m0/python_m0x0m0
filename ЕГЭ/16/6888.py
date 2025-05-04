from sys import setrecursionlimit
setrecursionlimit(4000)
def f(n):
    if n == 1: return 1
    if n > 1: return n + f(n-1)

k = 0
for n in range(1, 101):
    if f(2023)//f(n) % 2 == 0:
        k += 1
print(k)