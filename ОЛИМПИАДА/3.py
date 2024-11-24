n = int(input())
data = []

for _ in range(n):
    data.append(int(input()))
print(data)

d = 1
lens = []
for c in data:
    if c != 0:
        if d == 1:
            for _ in range(c):
                lens.append(1)
        elif d % 2 == 0:
            if c % 2 != 0:
                for _ in range(c + 1):
                    lens.append(d // 2)
            if c % 2 == 0:
                for _ in range(c):
                    lens.append(d // 2)
        elif d % 2 != 0:
            if c % 2 != 0:
                for _ in range(c + 1):
                    lens.append(d // 2)
                    lens.append(d // 2 + 1)
            if c % 2 == 0:
                for _ in range(c):
                    lens.append(d // 2)
                    lens.append(d // 2 + 1)

print(lens)
max_count = max(set(lens), key=lens.count)

if data.count(max_count) != lens.count(max_count):
    print(lens.count(max_count) + data.count(max_count))
else:
    print(lens.count(max_count))

print(max_count)