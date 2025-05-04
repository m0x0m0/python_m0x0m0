from math import sqrt
def f(n):
    return g(n-1)

def g(n):
    if n < 10: return n
    if n >= 10: return g(n-2) + 1
s = set()
for n in range(1, 101):
    if sqrt(f(n)) == int(sqrt(f(n))):
        s.add(n)
print(len(s))
