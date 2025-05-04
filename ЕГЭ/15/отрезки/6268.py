for x in [k * 0.25 for k in range(-10000, 10000)]:
    b = 23 <= x <= 37
    c = 41 <= x <= 73
    a = 0
    f = not(((not b) <= c) <= a)
    if f != 0:
        print(x)
# [23; 37] 14
# [41; 73] 32
# 50