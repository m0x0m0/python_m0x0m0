def f(n, t, k):
    if n > t + 1:
        return 0
    if n == t:
        return 1
    else:
        if k == 1:
            return f(n + 3, t, k - 1) + f(n * 2, t, k - 1)
        else:
            return f(n - 1, t, k + 1) + f(n + 3, t, k) + f(n * 2, t, k)
print(f(3, 12, 0))