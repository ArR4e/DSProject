def poisse_ja_tüdrukuid(järjend):
    vanused = [0,0]
    for i in range(len(järjend)):
        if järjend[i][-1] == "P":
            vanused[0] = vanused[0]+1
        else:
            vanused[1] = vanused[1]+1
    return tuple(vanused)
    


poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])