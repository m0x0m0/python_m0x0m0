from turtle import *
tracer(0)
k = 30

left(90)
for _ in range(12):
    fd(10 * k)
    right(216)
penup()
for x in range(-k , k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()