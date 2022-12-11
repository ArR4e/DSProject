def moos (karp_5L, karp_1L, moos_x_L):
    karpide_arv = 0 #lokaalne muutuja mille abil pärast karpide arvu tagastada saab
    if karp_5L >= 1 and moos_x_L >= 5: #kui moosi on rohkem kui 5l ja 5l karpe on, hakkab programm esmalt moosi nendesse karpidesse panema
        while karp_5L > 0 and moos_x_L >= 5:
            moos_x_L -= 5 #moosi jääb 5l vähemaks
            karp_5L -= 1 #üks viie liitrine karp kaob
            karpide_arv += 1 #üks karp karpide üldarvestuses tuleb juurde
    if moos_x_L >= 1 and karp_1L >= moos_x_L: #pärast 5l karpidega majandamist vaatab programm, kas on 1l karpe ka vaja
        while moos_x_L > 0:
            moos_x_L -= 1 #moos läheb maha
            karp_1L -=1 #üks liitrine karp kaob
            karpide_arv += 1 #karpide üldarvestuses karp juurde
    if moos_x_L == 0:
        return karpide_arv
    else: #juhul kui karbid saavad varem otse või moosi jääb üle, siis tagastab funktsioon -1
        return -1
        
    
        
suur_karp = int(input("Sisestage suurte karpide arv: ")) #küstiakse kasutajalt sisendid
väike_karp = int(input("Sisestage väikeste karpide arv: "))
moosi = int(input("Sisestage moosi kogus: "))
print(moos(suur_karp, väike_karp, moosi)) #käivitatakse funktsioon, mis võtab argumendiks karpide arvu ja moosi koguse