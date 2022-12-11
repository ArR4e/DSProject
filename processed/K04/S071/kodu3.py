# Kirjuta funktsioon, mis võtab argumentideks külgede arvu ning küljepikkuse, ning joonistab kilpkonnaga neile vastava korrapärase hulknurga.
# Joonista selle funktsiooni abil juhuslikesse ekraani kohtadesse juhusliku suuruse ja külgede arvuga 30 hulknurka.
from turtle import *
from random import *

def hulknurk(arv,pikkus):
    i = 0
    for i in range(arv):
        forward(pikkus)
        right(360 / arv)
        i += 1

j = 0
for j in range(30):
    kuhu = randint(50, 200)
    küljed = randint(4,20)
    pikk = randint(50,100)
    
    down()
    hulknurk(küljed,pikk)
    
    if kuhu // 2 == 0:
        up()
        forward(kuhu)
        left(60)
    else:
        up()
        backward(kuhu)
        right(45)
    
    j += 1

exitonclick()
