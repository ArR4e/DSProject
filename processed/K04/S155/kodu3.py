from turtle import*

nurki = int(input("mitu nurka uuel kujundil on "))
külg = int(input("Kui pikad on tal küljed  "))

nurk = ((nurki-2)*180) / nurki
sisenurk = 180 - nurk

i = 1

while i <= nurki:
    forward(külg)
    right(sisenurk)
    i = 1 + i 

exitonclick()