def f(n, t):
    if n > t: return 0
    elif n == t: return 1
    return f(n+1, t) + f(n+3, t) + f(n*3, t)
print(f(4, 10) * f(10, 17) * f(17, 23))