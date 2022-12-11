# 3. Hulknurgad

# Kirjuta funktsioon, mis võtab argumentideks külgede arvu ning küljepikkuse, ning joonistab kilpkonnaga neile vastava korrapärase hulknurga.

# Joonista selle funktsiooni abil juhuslikesse ekraani kohtadesse juhusliku suuruse ja külgede arvuga 30 hulknurka.

# Automaatkontroll on olemas, aga ei kontrolli väljundpildi korrektsust.

from math import *
from turtle import *
from random import randint

def nurga_joonis(n, a):
    sisenurk = 180*(n-2)/n
    valisnurk = 180-sisenurk

    while n > 0:
        down()
        forward(a)
        left(valisnurk)
        n -= 1
    

kujund_n = 30

while kujund_n > 0:
    up()
    x = randint(-200, 200)
    y = randint(-200, 200)
    setposition(x, y)
    down()    
    n = randint(3, 20)
    a = randint(10, 100)
    nurga_joonis(n, a)
    
    kujund_n -= 1

exitonclick()
