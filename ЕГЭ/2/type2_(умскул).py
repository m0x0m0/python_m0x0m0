print('y x w z')
for y in range(2):
    for x in range(2):
        for w in range(2):
            for z in range(2):
                if (((not(y)) or x) and w and (not(z))) == 1:
                    print(y, x, w, z)
