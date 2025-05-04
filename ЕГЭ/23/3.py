def f(n, t):
    if n > t or n == 26: return 0
    elif n == t: return 1
    return f(n+1, t) + f(2*n+1, t)
print(f(1, 27))