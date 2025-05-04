for x in [k * 0.25 for k in range(0, 10000)]:
    p = 52 <= x <= 105
    q = 0 <= x <= 53
    a = 0
    f = (((not p) and (not q) and (not a)) <= (x*x > 303601))
    if f != 1:
        print(a)