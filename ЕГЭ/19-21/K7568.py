'''
+1
*2
win when p + s >= 227
start when p = 17, 1 <= s <= 209
'''
def f(p, s, n):
    if (s + p >= 227 and (n == 4 or n == 2)):
        return 1
    elif (s + p >= 227 and n < 4) or (s + p < 227 and n == 4):
        return 0
    if n % 2 == 0:
        return f(p+1, s, n+1) and f(p*2, s, n+1) and f(p, s+1, n+1) and f(p, s*2, n+1)
    else:
        return f(p + 1, s, n + 1) or f(p * 2, s, n + 1) or f(p, s + 1, n + 1) or f(p, s * 2, n + 1)

for i in range(1, 209):
    if f(17, i, 0):
        print(i)
        break

#19: 53
#20: 96 104
#21: 95