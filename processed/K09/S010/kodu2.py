from random import randint  # Automaatkontroll jookseb selle ülesande kontrollimisel miskipärast kokku.
from math import floor
def minu_shuffle(a):    # Kui kutsuda funktsioon välja, muudab see listi vastavalt ülesandele ning ei tagasta uut listi. Peaks minu hinnangul olema õigesti lahendatud. 
    eelmine_suvaindeks=0
    suvaindeks=randint(0, len(a)-1)
    eelmine_asuva=0
    i=0
    while i < floor(len(a)/2):
        suvaindeks=randint(0, len(a)-1)
        if suvaindeks==eelmine_suvaindeks or suvaindeks==i or eelmine_asuva==a[suvaindeks]:
            continue
        algne_a=a[i]
        a[i]=a[suvaindeks]
        a[suvaindeks]=algne_a
        eelmine_asuva=a[suvaindeks]
        eelmine_suvaindeks=suvaindeks
        i+=1