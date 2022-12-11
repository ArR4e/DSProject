import os

km = float(input("Sisesta teepikkus kilomeetrites: "))

f = open("taksohinnad.txt", encoding="UTF-8")

faili_suurus = os.path.getsize("taksohinnad.txt")
if faili_suurus > 0:

    def andmed(f):

        nimed = []
        sisse_hind = []
        km_hind = []
        
        for rida in f:
            
            rida = rida.strip()
            pikkus = len(rida)
            
            komakoht1 = rida.find(",")
            komakoht2 = rida.rfind(",")
            
            nimed.append(rida[0:komakoht1])
            sisse_hind.append(rida[komakoht1+1:komakoht2])
            km_hind.append(rida[komakoht2+1:pikkus])
            
        def parim_hind(nimed, sisse_hind, km_hind, km):
            
            i = 0
            parim_hind = 100000 #paneme mingi ulmelise algse parima hinna, milleni reaalne hind kunagi ei pürgi
            while i < len(nimed):
                hind_kokku = float(sisse_hind[i]) + float(km_hind[i]) * km
                if hind_kokku < parim_hind:
                    parim_hind = hind_kokku
                    parim_takso = nimed[i]
                i += 1
            print("Kõige odavam on " + parim_takso + ".")
                
        parim_hind(nimed, sisse_hind, km_hind, km)
        
    andmed(f)

else:
    print("Fail on tühi.")


        
        