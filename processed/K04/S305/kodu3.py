import turtle

def hulknurk(a, p):
    
    nurk = ((a-2)*180)/a
    turtle.getscreen()
    turtle.speed(10)
    
    while a > 0:
        turtle.fd(p)
        turtle.rt(180-nurk)
        a -= 1
    
    turtle.exitonclick()
    
arv = int(input("Külgede arv: "))
pikkus = int(input("Küljepikkus: "))

hulknurk(arv, pikkus)