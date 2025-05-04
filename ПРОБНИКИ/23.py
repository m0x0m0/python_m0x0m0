def f(x, t):
    if x == t:
        return 1
    if x < t:
        return 0
    else:
        return f(x-1, t) + f(x//2, t)
print(f(30, 12) * f(12, 1))