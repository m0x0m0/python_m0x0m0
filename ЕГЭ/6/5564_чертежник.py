from turtle import *
screensize(3000, 3000)
tracer(0)
k = 30
for _ in range(8):
    goto((xcor() + 3) * k, ycor() + 6 * k)
    goto(xcor() + 8 * k, ycor() - 5 * k)
    goto(xcor() - 5 * k, ycor() - 3 * k)
    goto(xcor() - 6 * k, ycor() + 2 * k)
pu()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(5)
done()