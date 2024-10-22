a, b, c, x = 0, 0, 0, 0
x = 0
a, b, c = int(input()), int(input()), int(input()),
while c - a != 2:
    x = x + 1
    if b - a > c - b:
        c = b
    else:
        a = b
    b = c - (c - a) // 2
print(x)