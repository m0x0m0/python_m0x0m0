from turtle import *

k = 30
tracer(0)
left(90)

for i in range(3):
    fd(10 * k)
    right(120)
pu()
fd(10 * k)
right(90)
fd(3 * k)
pd()
for j in range(4):
    fd(10 * k)
    right(90)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)

done()
