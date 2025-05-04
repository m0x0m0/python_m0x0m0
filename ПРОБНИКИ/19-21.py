'''
+1 *2
START: d = 7, 1 <= s <= 73
WIN: d + s >= 81
'''

def f(s, d, n):
    if s + d >= 81 and (n == 4 or n == 2):
        return 1
    if (s + d >= 81 and n < 4) or (s + d < 81 and n == 4):
        return 0
    else:
        if n % 2 == 0:
            return f(s+1, d, n+1) and f(s*2, d, n+1) and f(s, d+1, n+1) and f(s, d*2, n+1)
        else:
            return f(s + 1, d, n + 1) or f(s * 2, d, n + 1) or f(s, d + 1, n + 1) or f(s, d * 2, n + 1)
for i in range (1, 74):
    if f(i, 7, 0): print(i)

# 19: 19
# 20: 33 36
# 21: 32
