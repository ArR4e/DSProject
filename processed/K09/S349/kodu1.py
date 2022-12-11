import matplotlib.pyplot as plt
import numpy as np

def numbrid(andmed):
    fail = open(andmed, encoding = "UTF-8")
    aktsiad = []
    for rida in fail:
        rida = rida.strip()
        rida_pooleks = rida.split(", ")
        kuupäev = rida_pooleks[0]
        aktsia_hind = rida_pooleks[1]
        aktsiad.append(float(aktsia_hind))
    return aktsiad
    fail.close()
    
def silu_andmed(aktsiad, täisarv):
    uus_järjend = []
    summa = 0
    summa_järjend = []
    lugeja = 0
    for element in aktsiad:
        vastava_koha_jagatis = 1/element
        summa = summa + vastava_koha_jagatis
        summa_järjend.append(vastava_koha_jagatis)
        if lugeja < täisarv:
            lugeja = lugeja + 1
            uus_element = lugeja / summa
            uus_järjend.append(uus_element)
        elif lugeja == täisarv:
            lugeja = täisarv
            järjendi_summa = sum(summa_järjend[(-(täisarv)):])
            uus_element = lugeja / järjendi_summa
            uus_järjend.append(uus_element)
            
    return uus_järjend

    
#graafikuga on probleeme
    fig = plt.figure()          
    x = [0.0000,0.0025,0.0050,0.0075,0.0100,0.0125,0.0150,0.0175]
    y = [len
    ax = fig.add_subplot(1,1,1)
    ax.plot(uus_järjendaktsiad, uus_järjend)
    ax.set_xlabel("Aktsiad")
    ax.set_ylim(0, 0.0175)         # Määrame y-telje nähtavuspiirkonna
    ax.set_xticks([200,400,600,800,1000])  # ja x-telje märgid
    
    plt.show()
     
täisarv = int(input("Sisesta täisarv: "))
andmed= input("Sisesta faili nimi: ")
print(silu_andmed((numbrid(andmed)), täisarv))
