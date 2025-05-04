for x in[k*0.25 for k in range(-10000, 10000)]:
    p = 43 <= x <= 49
    q = 44 <= x <= 53
    a = 1
    f = (a <= p) or q
    if f != 0:
        print(x)
# [43; 53]
# 10