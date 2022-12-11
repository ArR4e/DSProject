f=open("lapsed.txt")
ff=open("nimed.txt")
vanem_laps={}
tulemus={}
vanemad={}
#laps="Robert Peedumets"
def seosta_lapsed_ja_vanemad(f,ff,lapz):
    for i in f.readlines():
        koodid=i.split(" ")
        vanem=koodid[0].strip()
        laps=koodid[1].strip()
        if laps in vanem_laps:
            vanem_laps[laps].append(vanem)
        if laps not in vanem_laps:
            vanem_laps[laps]=[vanem]
            
    for i in ff.readlines():
        koodid=i.split(" ")
        nimi=koodid[1].strip()+(" ")+koodid[2].strip()
        isikukood=koodid[0].strip()
        tulemus[isikukood]=nimi
        
    for key, value in tulemus.items():
        if lapz == value:
            temavanemad=vanem_laps[key]
            esimene=tulemus[temavanemad[0]]
            if len(temavanemad) >= 2:
                teine=tulemus[temavanemad[1]]
                vanemad[lapz]={esimene,teine}
            else:
                vanemad[lapz]={esimene}
            return vanemad
        
print(seosta_lapsed_ja_vanemad(f,ff,laps))

f.close()
ff.close()