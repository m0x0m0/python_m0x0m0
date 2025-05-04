for x in [k * 0.25 for k in range(-10000, 10000)]:
    d = 7 <= x <= 68
    c = 29 <= x <= 100
    a = 0
    f = d <= (((not c) and (not a)) <= (not d))
    if f != 1:
        print(x)