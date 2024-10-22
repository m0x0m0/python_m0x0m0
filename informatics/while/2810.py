numbers = input().split()
numbers.remove('0')
count = 0

for num in numbers:
    if int(num) % 2 == 0:
        count += 1
print(count)