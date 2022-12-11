from random import randint
def minu_shuffle(järjend):
    for element in järjend:
        viimane=(len(järjend)-1)
        juhuslik_arv=randint(1, viimane)
        järjend[0], järjend[juhuslik_arv]=järjend[juhuslik_arv],järjend[0]
#ma ei oska seda elementi kuidagi tsüklisse haarata, sellepärast ei töötagi
järjend=[1, 2, 3, 4, 5]
vastus=minu_shuffle(järjend)
print(vastus)
