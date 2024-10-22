from turtle import *
screensize(3000, 3000)
tracer(0)
left(90)
pu()
k = 20
for _ in range(3):
    pd()
    for _ in range(2):
        fd(10 * k)
        right(90)
        fd(10 * k)
        right(90)
    pu()
    fd(10 * k)
    right(90)
    fd(5 * k)
    left(90)
pu()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(5)
done()



