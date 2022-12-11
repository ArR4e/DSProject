#+


def poisse_ja_tüdrukuid(järjend):
    poisid=0
    tüdrukud=0
    k=0
    while k<len(järjend):
        for rida in järjend:
            uus_järjend = rida.split(" ")
            k+=1
            
            if uus_järjend[-1] == "P":
                poisid += 1
            else:
                tüdrukud += 1
    return (poisid, tüdrukud)

järjend=['Mati P', 'Kati T', 'Siim Aleksander P', 'Jüri P', 'Veronika T', "Karl P"]

poisse_ja_tüdrukuid(järjend)

