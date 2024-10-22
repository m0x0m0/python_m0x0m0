n = int(input())
num = 1
count = 0

for i in range(1, n+1):
    print(num, end=' ')
    count += 1
    if num == count:
        num += 1
        count = 0