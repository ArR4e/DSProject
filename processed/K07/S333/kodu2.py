def hinna_kalkulaator(a,b):
    #a on sisseistumine
    #b on kilomeeter
    hind= a+b*tee_pikkus
    return hind
nimed= [] #esmalt tühjad järjendid, et oleks kuhu liita
sisseistumine= []
kilomeeter= []
arvutatud_hinnad= []

hinnad=open('taksohinnad.txt',encoding='UTF-8')

tee_pikkus= float(input('Sisesta tee pikkus kilomeetrites: '))
#tee_pikkus= 7 peale testimist peaks ikka tagasi panema sisendi küsimise

#loeme faili andmed sisse järjenditesse
for rida in hinnad: #loeme faili tsükliga läbi, siis pole vaja koodi korrata
    rida= rida.strip('\n').split(',') #teame,et reas on eraldajaks koma, teeme järjendi, eemaldab \n
    nimed= nimed+ [rida[0]] #tekitame nimedest järjendi liitmisel nurksulud, siis saab aru,et järjend
    sisseistumine= sisseistumine +[float(rida[1])] #muudame kohe hinnad ujukomaks ka
    kilomeeter= kilomeeter+ [float(rida[2])]
hinnad.close() #siin võib faili kinni panna, andmed on juba käes

#arvutame iga pakkuja hinna ja salvestame need järjendisse
i=0 #abimuutuja järjendi indeksi jaoks
while i< len(nimed): #seni kuni on veel järjendis nimesid, jätkab
    hind= hinna_kalkulaator(sisseistumine[i],kilomeeter[i])#arvutab hinna indeksile vastavalt
    arvutatud_hinnad= arvutatud_hinnad + [hind]
    i+=1
i=0 #nullime abimuutuja, ei hakka uut võtma

#leiame kõige odavama pakkuja
for hind_min in arvutatud_hinnad: #muutuja hind on tsükliväliselt ka kasutuses , hea oleks tegelikult uus nimi
    if hind_min == min(arvutatud_hinnad):
        print(' Kõige odavam on ',nimed[i], 'hinnaga',hind_min,'€.')
    else: #kui arvutatud hind pole kõige väiksemaga võrdne
        i+=1 # siis suurendame indeksit, et väljastusel oleks õige takso nimi

        
    
    