from turtle import *
left(90)
tracer(0)
k = 20
screensize(7000, 5000)

for _ in range(2):
    fd(24*k)
    rt(90)
    fd(10*k)
    rt(90)
up()
fd(5*k)
lt(90)
fd(12*k)
rt(90)
down()
for _ in range(2):
    fd(9*k)
    rt(90)
    fd(35*k)
    rt(90)
pu()
for x in range(-k*10, k*10):
    for y in range(-k, k):
        goto(x*k, y*k)
        dot(5)
done()
