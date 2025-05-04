s = set()
def f(n, c):
    if c > 11: return 0
    if c == 11:
        s.add(n)
        return 1
    if c < 11:
        f(n-1, c+1)
        f(n-5, c+1)
        f(n*2, c+1)
f(2, 0)
print(len(s))
