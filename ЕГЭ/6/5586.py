from turtle import *

tracer(0)
left(90)
k = 30
for _ in range(100):
    fd(10 * k)
    right(180)
    fd(10 * k)
    right(190)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()