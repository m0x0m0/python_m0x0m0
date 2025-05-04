maxi = 0
def f(num):
    res = ''
    while num > 0:
        res = str(num%3) + res
        num //= 3
    return res
l = []
for x in range(2031, 1, -1):
    n = 3**100 - x
    if f(n).count('0') == 1:
        l.append(x)
print(l)