for x in[k*0.25 for k in range(-10000, 10000)]:
    p = 17 <= x <= 58
    q = 29 <= x <= 80
    a = 0
    f = (p <= ((q and (not a)) <= (not(p))))
    if f != 1:
        print(x)

# 11
# 29