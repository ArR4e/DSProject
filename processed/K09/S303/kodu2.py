from random import choice

def minu_shuffle(jarjend):
    jarjendi_indeksid = list(range(len(jarjend)))
    jarjendi_koopia = jarjend[:]
    jarjend.clear()
    
    while jarjendi_koopia:
        indeks = choice(jarjendi_indeksid)
        elm = choice(jarjendi_koopia)
        jarjend.insert(indeks, elm)
        jarjendi_koopia.remove(elm)