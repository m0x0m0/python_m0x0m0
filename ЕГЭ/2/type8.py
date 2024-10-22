print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = bool(((y <= w) == (x <= (not(z)))) and (x or w))
                print(x, y, z, w, F)

0 0 0 0 False
0 0 0 1 True
0 0 1 0 False
0 0 1 1 True
0 1 0 0 False
0 1 0 1 True
0 1 1 0 False
0 1 1 1 True
1 0 0 0 True
1 0 0 1 True
1 0 1 0 False
1 0 1 1 False
1 1 0 0 False
1 1 0 1 True
1 1 1 0 True
1 1 1 1 False