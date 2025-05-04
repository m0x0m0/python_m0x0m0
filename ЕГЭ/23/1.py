def f(n, t):
    if n < t:
        return 0
    elif n == t:
         return 1
    else:
        return f(n-2, t) + f(n//2, t)

print(f(38, 16)*f(16, 2))
