from turtle import *
screensize(3000, 3000)
tracer(0)
left(90)
k = 20

right(180)
fd(3 * k)
right(90)
fd(48 * k)
right(90)
fd(3 * k)
for _ in range(6):
    seth(90)
    circle(-4 * k, 180)

pu()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(5)
done()