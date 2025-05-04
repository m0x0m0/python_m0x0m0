from turtle import *
tracer(0)
k = 30
screensize(2000, 6000)
lt(90)

for i in range(9):
    fd(27*k)
    rt(90)
    fd(30*k)
    rt(90)
pu()
fd(3*k)
rt(90)
fd(6*k)
lt(90)

pd()
for i in range(9):
    fd(77*k)
    rt(90)
    fd(66*k)
    rt(90)
pu()
for x in range(-200, 200):
    for y in range(-k, k):
        goto(x*k, y*k)
        dot(3)


done()
