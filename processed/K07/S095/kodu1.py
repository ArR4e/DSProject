def poisse_ja_tüdrukuid(arr):
    poiss_tydruk=()
    poisse=0
    tydrukuid=0
    poiss=" P"
    tüdruk=" T"
    for x in arr:
        if x.endswith(poiss):
            poisse+=1
        elif x.endswith(tüdruk):
            tydrukuid+=1
    poiss_tydruk=list(poiss_tydruk)
    poiss_tydruk.insert(0, poisse)
    poiss_tydruk.insert(1, tydrukuid)
    poiss_tydruk=tuple(poiss_tydruk)
    return poiss_tydruk
# poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])
# print(poiss_tydruk)