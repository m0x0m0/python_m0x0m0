'''from turtle import *
tracer(0)
left(90)
k = 30
s = 4
for _ in range(2):
    fd(3*s * k)
    right(90)
    fd(s * k)
    right(90)
    for j in range(2):
        fd(s * k)
        left(90)
    for i in range(2):
        fd(s * k)
        right(90)
pu()
for s in range(-k, k):
    for y in range(-k, k):
        goto(s * k, y * k)
        dot(5)
done()'''

for x in range(1, 200):
    if (2 * (x - 1) * (3 * x - 1)) + ((x - 1) * (x + 1)) > 200000:
        print(x)
        break