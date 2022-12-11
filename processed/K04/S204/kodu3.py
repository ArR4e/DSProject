from turtle import *
n = int(input("Palun sisesta külgede arv:"))
külg = float(input("Palun sisesta küljepikkus:"))

summa = 1

summa += 1

while summa < 31:
    summa += 1
    
   


    def hulknurk(n,külg):
    
        i = 0
        while i < n:
            forward(külg)
            left(360/n)
            i += 1

    hulknurk(n,külg)

    up()
    forward(22)
    left(10)
    forward(12)
    down()
        
        
    
        


exitonclick()