def d(l, m): return l % m == 0

def f(x, a): return ((d(x, 10) and d(x, 26) and (x >= 300)) <= (a <= x))

print(max(a for a in range(0, 1000) if all(f(x, a) == 1 for x in range(1, 2000))))