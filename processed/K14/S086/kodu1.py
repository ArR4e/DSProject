#Võtab ette järjendi/arvu ja kõik arvud seal sees tagastatakse enda absoluutväärtusena
#Muutuja võib olla järjend või arv ja selle elementideks samuti järjendid või arvud

def rek_abs(sisend):
    if isinstance(sisend, (int, float)):
        return abs(sisend)
    elif isinstance(sisend, (list, tuple)):
        väljund = []
        for element in sisend:
            väljund.append(rek_abs(element))
        return väljund
    