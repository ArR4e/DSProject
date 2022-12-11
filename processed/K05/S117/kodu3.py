#alustasin 28.09.2021 (21:11)

def moos(suur, väike, kogus):
    kasutatud = 0
    while kogus >= 5 and suur > 0:
        kogus -= 5
        suur -=1
        kasutatud +=1
    if väike >= kogus:
        return(kasutatud + kogus)
    elif kogus == 0:
        return(kasutatud)
    else:
        return -1