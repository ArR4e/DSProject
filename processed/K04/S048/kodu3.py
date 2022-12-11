from turtle import*


külje_arv = int(input("Sisestage külje arv: "))
külje_pikkus = int(input("Sisestage külje pikkus: "))

n = 360/külje_arv
i = 0

while True i == külje_arv:
    
    forward(külje_pikkus)
    right(n)
i = i+1