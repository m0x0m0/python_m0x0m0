print('y x z')
for y in range(2):
    for x in range(2):
        for z in range(2):
            if ((x == y) or (x <= (z and y))) == 0:
                print(y, x, z)
