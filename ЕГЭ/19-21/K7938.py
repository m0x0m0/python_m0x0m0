'''
+3
+6
*3
win >= 132
1 <= S <= 131
'''
def f(s, n):
    if (s > 131 and (n == 4 or n == 2)):
        return 1
    elif ((s < 132 and n == 4) or (s > 131 and n < 4) or n > 4):
        return 0
    if n % 2:
        return f(s+3, n+1) or f(s+6, n+1) or f(s*3, n+1)
    else:
        return f(s + 3, n + 1) and f(s + 6, n + 1) and f(s * 3, n + 1)

for i in range(1, 132):
    if f(i, 0):
        print(i)

#19: 41
#20: 14 35
#21: 32