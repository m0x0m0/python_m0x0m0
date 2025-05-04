for x in [k*0.25 for k in range(-10000, 10000)]:
    p = 3 <= x <= 15
    q = 14 <= x <= 25
    a = 1
    f = (p == q) <= (not a)
    if f != 0:
        print(x)
# [3; 14) / (15; 25]
#    11   / 10
 