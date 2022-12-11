from random import randint

def minu_shuffle(järjend):
    if järjend != []:
        for i in range(20): #elementide vahetus 20 korda
            kust = randint(0, len(järjend)-1) #valib suvaliselt ühe elemendi
            arv1 = järjend[kust]
            kuhu = randint(0, len(järjend)-1) #valib suvaliselt teise elemendi
            arv2 = järjend[kuhu]
            
            if kust == kuhu: #kui valitud sama element, ei tee miskit
                continue
            else: #kui valitud erinevatelt kohtadelt element, ss tehakse vahetus
                järjend[kust] = arv2
                järjend[kuhu] = arv1