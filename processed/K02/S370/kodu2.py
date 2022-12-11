from math import *

pik=int(input("Kui pikk on elektriliin?"))
kau=int(input("Kui kaugel postid üksteisest asuvad?"))

print("Vaja läheb minimaalselt", str(ceil(pik/kau)), "posti")

