def poisse_ja_tüdrukuid(järjend):
    x = 0
    y = 0
    for rida in järjend:
        uus_järjend = rida.split(" ")
        x += uus_järjend.count('P')
        y += uus_järjend.count('T')
        
    return(x, y)

# poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T'])