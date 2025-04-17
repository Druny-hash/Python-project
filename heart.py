import math
from turtle import *

def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(10000000000000)
bgcolor("black")

def new_func():
    new_func1()

def new_func1():
    goto(0, 0)

for i in range(100000):
    goto(hearta(i) * 20, heartb(i) * 20)
    for j in range(5):
        color("red")
        new_func()
        

