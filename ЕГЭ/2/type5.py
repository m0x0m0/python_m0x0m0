print('x z y w')
for x in range(2):
    for z in range(2):
        for y in range(2):
            for w in range(2):
                if ((x and z) or ((z <= y) <= (w <= x))) == 0:
                    print(x, z, y, w)