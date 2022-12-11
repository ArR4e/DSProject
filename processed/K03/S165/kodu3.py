arv = int(input("Palun sisestage siia naturaalarv n: "))
i = 0
RuutudeSumma = 0
SummaRuut = 0
while i < arv:
    a = arv - (arv-(i + 1))
    RuutudeSumma = RuutudeSumma + a**2
    i += 1

i = 0
 
while i < arv:
    b = arv - (arv-(i + 1))
    SummaRuut = SummaRuut + b
    i += 1
    
SummaRuut = SummaRuut**2

vastus = SummaRuut - RuutudeSumma

print(" esimese n naturaalarvu summa ruudu ja ruutude summa erinevus on", vastus)
    



