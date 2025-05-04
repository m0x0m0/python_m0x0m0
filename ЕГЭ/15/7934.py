for a in range(0, 100):
    if all(((x-3*y)<a) or (y>400) or (x>56) for x in range(1, 100) for y in range(1, 100)):
        print(a)