from turtle import *

tracer(False)
lt(90)
rt(45)
k = 25 # Масштабирование. Если не умножать на коэффициент, рисунок получится очень маленьким
for i in range(3):
    rt(45)
    fd(10 * k)
    rt(45)
rt(315)
fd(10 * k)
rt(90)
fd(20*k)
rt(90)
for i in range(2):
    fd(10*k)
    rt(90)
penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(5, "red")

done()


