from turtle import *

tracer(0) #отключение анимации
left(90) #поворот головы черепахи на 90 градусов
k = 30

right(30)
for _ in range(30):
    right(30)
    forward(3 * k)
    right(30)
penup()

for x in range(-k, k):
    for y in range(-k, k):
        setpos(x * k, y * k)
        dot(5)
done()
