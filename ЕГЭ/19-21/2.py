'''
+1 *2
win >=46
1 <= S <= 45
'''

def f(s, m):
    if m == 3 and s >= 46:
        return 1
    elif m == 3 and s < 46:
        return 0
    elif m < 3 and s >= 46:
        return 0
    else:
        if m % 2:
            return f(s + 1, m + 1) and f(s * 2, m + 1)
        else:
            return f(s + 1, m + 1) or f(s * 2, m + 1)
for i in range(1, 46):
    if f(i, 0):
        print(i)