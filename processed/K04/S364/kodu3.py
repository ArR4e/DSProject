from turtle import*
import random
def hulknurgad (kylgede_arv, kylgede_pikkus):
    speed(5)
    penup()
    x = random.randint(5,400)
    z = random.randint(5,400)
    goto(x,z)
    pendown()
    begin_fill()
    for i in range(kylgede_arv):
        forward (kylgede_pikkus)
        left (360/kylgede_arv)
    end_fill()
for i in range(30):
    kylgede_arv = random.randint(4,8)
    kylgede_pikkus = random.randint(30,170)
    hulknurgad(kylgede_arv, kylgede_pikkus)