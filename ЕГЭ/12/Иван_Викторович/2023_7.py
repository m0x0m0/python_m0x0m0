maxi = 0
for i in range(185, 1000):
    s = '1' * i
    while '1111' in s:
        s = s.replace('1111', '2', 1)
        s = s.replace('22', '11', 1)
    if s.count('1') > maxi:
        maxi = s.count('1')
        min_i = i
print(min_i)
