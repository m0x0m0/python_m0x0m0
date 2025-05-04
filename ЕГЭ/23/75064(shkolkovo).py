s = set()
def f(n, c, k1, k2):
    if c > 11: return 0
    if c == 11:
        s.add(n)
        return
    if c < 11 and k1 < 3 and k2 < 3:
        f(n+2, c+1, k1+1, k2)
        f(n * 2, c + 1, k1, k2 + 1)
f(1, 0, 0, 0)
print(len(s))