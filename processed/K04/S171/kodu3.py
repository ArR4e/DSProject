from turtle import*
from random import*

n = int(input())
a = int(input())
def hulknurk(x, y):
    for i in range(0,x):
        forward(y)
        right(180-(x-2)*(180/x))
    
#for y in range (0, 30):
#    up()
#    setposition(randint(-500, 500),randint(-300, 300))
#    down()
#    a = randint(10, 100)
#    n = randint(3,10)
hulknurk(n, a)
    


