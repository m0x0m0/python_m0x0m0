from turtle import *
screensize(3000, 3000)
tracer(0)
left(90)
k = 30
for _ in range(2):
    fd(10 * k)
    right(90)
    fd(20 * k)
    right(90)
pu()
fd(5 * k)
right(90)
fd(7 * k)
left(90)
pd()
for _ in range(2):
    fd(20 * k)
    right(90)
    fd(40 * k)
    right(90)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()
