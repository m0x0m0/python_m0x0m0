for a in range(1, 40):
    for b in range(1, 40):
        for c in range(1, 40):
            s = '0' + '1' * a + '2' * b + '3' * c + '0'
            while '00' not in s:
                s = s.replace('01', '210', 1)
                s = s.replace('02', '3101', 1)
                s = s.replace('03', '2012', 1)
            if s.count('1') == 111 and s.count('2') == 101 and s.count('3') == 35:
                print(a + b + c + 2)
                break