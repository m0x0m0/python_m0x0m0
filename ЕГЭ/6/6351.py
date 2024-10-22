from turtle import *
tracer(0)
left(90)
k = 30
x = 3
for _ in range(4):
    fd(x * k)
    right(90)
    fd(x * k)
    left(90)
    fd(x * k)
    right(90)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()
