def f(n):
    if n > 2 * 10**6: return n
    return 7*n + f(3*n)

def g(n):
    return f(n) / n

k = 0
for n in range(1, 10**5):
    if g(n) == g(12345):
        k += 1
print(k)
