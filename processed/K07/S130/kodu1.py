def poisse_ja_tüdrukuid(järjend):
    P = 0
    T = 0
    for rida in järjend:
        uus_järjend= rida.split(" ")
        x = uus_järjend[-1]
        if x == 'P':
            P += 1
        else:
            T += 1
        
    return (P,T)


print(poisse_ja_tüdrukuid(['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veroonika T']))