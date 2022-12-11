fail = open("taksohinnad.txt", 'r')
järjend = fail.readlines()
fail.close()

vahemaa = float(input("Sisesta teepikkus kilomeetrites:"))
hind = 0
takso = []
hinnad = []
if järjend != []:
    for i in järjend:
        i = i.strip('\n')
        i = i.split(',') #eraldab komaga
        i[1] = float(i[1]) #järjendi esimese liikme teisendamine ujukomaarvuks
        i[2] = float(i[2])
        hind = i[1] + i[2]*vahemaa
        hinnad.append(hind) #lisab listi hind - vastava nr
        takso.append(i[0])
    
    odavaim = min(hinnad)
    koht = hinnad.index(odavaim)
    takso_firma = takso[koht]
    print("Kõige odavam on", takso_firma)
else:
    print("puudub")
        
        