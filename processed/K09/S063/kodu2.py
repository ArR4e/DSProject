import random
########################################################################################################
### Kirjuta funktsiooni 'shuffle' analoogne funktsioon 'minu_shuffle',                               ###
### mis ajab argumendiks antud järjendis elementide järjekorra juhuslikult segamini.                 ###
########################################################################################################
def minu_shuffle(järjend):
    # iga järjendi indeksi järgi
    for i in range(len(järjend)):
        while True:
            # kui juhuslikult valitud indeks pole jooksev indeks
            # siis nende indeksite elemente ümber vahetada
            rnd_i = random.choice(range(len(järjend)))
            if rnd_i != i:
                el = järjend[i]
                järjend[i] = järjend[rnd_i]
                järjend[rnd_i] = el
                break
    return järjend
########################################################################################################
