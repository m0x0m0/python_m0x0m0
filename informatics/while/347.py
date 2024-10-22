n = int(input())
count = 0
for i in range(n):
    n = int(input())
    if n == 0:
        count += 1
if count == 0:
    print('NO')
else:
    print('YES')