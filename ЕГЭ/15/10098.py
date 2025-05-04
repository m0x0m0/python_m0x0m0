def f(x, y, a):
    return (x + 2*y < a) or (y > x) or (x > 60)
print(min(a for a in range(0, 200) if all(f(x, y, a) == 1 for x in range(0, 2000) for y in range(0, 2000))))