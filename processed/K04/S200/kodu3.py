from turtle import*

arv= int(input("Sisesta külgede arv: "))
pikkus = int(input("Sisesta külgede pikkus: "))

def hulknurk(a,b):
    joonistatud = 0
    while joonistatud < a:
        forward(b)
        nurgad = 360/a
        left(nurgad)
        joonistatud += 1

hulknurk(arv,pikkus)
exitonclick()