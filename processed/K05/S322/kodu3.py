
def moos(suured, väikesed, moosi_kg):
    # defineeri muutuja 'suuri', et jälgida mitu suurt karpi on alles
    suuri = suured
    # defineeri see muutuja, et jälgida kui palju moosi veel alles on
    allesolev_moos = moosi_kg
    # defineeri see muutuja, et hiljem väljastada, mitu karpi oli vaja
    karpe = 0
    # käi läbi kõik suured karbid
    # lõpeta tsükkel kui moosi on liiga vähe või kui suured karbid
    # saavad otsa
    while suuri > 0 and allesolev_moos >= 5:
        allesolev_moos -= 5
        suuri -= 1
        karpe += 1
    # kui väikeseid karpe on vähem kui moosi koguse
    # mahutamiseks vaja läheb, siis lõpeta kohe
    # funktsioon ja tagasta -1
    if väikesed < allesolev_moos:
        return -1
    # mahuta moos väikestesse karpidesse
    while allesolev_moos > 0:
        allesolev_moos -= 1
        karpe += 1
    # tagasta karpide arv
    return karpe
