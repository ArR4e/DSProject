import math

L = int(input('Sisestage Liini pikkus: '))  #liinipikkus

PMK =int(input('Sisestage kõrvutiseisvate postide maksimaalkaugus: ')) #postide maksimaal kaugus

postide_arv = (L/PMK)+1

print(math.ceil(postide_arv))