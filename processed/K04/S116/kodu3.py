from turtle import*
from random import randrange

h = 1
while h <= 30:
    h += 1
    küljed = randrange(3,7) #piirasin suvalise arvu range'i, et pildi pealt midagi aru ka saada oleks.
    küljepikkus = randrange(50,100)

    def joonis(küljed, küljepikkus):
        i = 0
        penup()
        right(randrange(1,360))
        forward(randrange(50,100))
        pendown()
        while i < küljed:
            i += 1
            forward(küljepikkus)
            right(360/küljed)
            
        
    print(joonis(küljed, küljepikkus))
exitonclick()

### Siin on ülesande esimese poole lahendus
#
#
#from turtle import*
#
#küljed = int(input("Külgede arv: "))
#küljepikkus = float(input("Küljepikkus: "))
#
#def joonis(küljed, küljepikkus):
#    i = 0
#    while i < küljed:
#        i += 1
#        forward(küljepikkus)
#        right(360/küljed)
#        
#print(joonis(küljed, küljepikkus))
#exitonclick()

