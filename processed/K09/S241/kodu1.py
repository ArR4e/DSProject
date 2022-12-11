from statistics import harmonic_mean
failinimi = "aktsiad.txt" 
perioodi_pikkus = int(input("Sisesta perioodi pikkus: "))  # selle perioodi pikkus, mille kohta soovime arvutada keskmisi
def silu_andmed(andmed, perioodi_pikkus):
    with open(andmed) as fail: # avan faili nii, et ei pea seda eraldi sulgema
        aktsiahinnad = [] # tühi järjend, mille sisse hakkavad minema igalt realt loetud aktsiahinnad
        for rida in fail: # loen iga rea failis, st loen faili ridahaaval
            rida = rida.strip().split(', ') # strip on sõne meetod, eemaldab tühikud eest ja tagant ja split on sõne meetod, mis teeb sõnest järjendi 
            aktsiahinnad.append(float(rida[1])) # järjendi aktsiahinnad sisustamine float-tüüpi elemenditega toimub siin
    pikkus = len(aktsiahinnad) # aktsiahindade arv, vajalik hiljem
    keskmised = [] # tühi järjend, kuhu hakkavad minema keskmiste väärtused
    for i in range(pikkus): #keskmised tuleb arvutada nii, et kõik aktsiahinnad oleksid sees ja see tsükkel alsutab esimesest ja lõpetab viimasega
        periood = aktsiahinnad[i:i+perioodi_pikkus] #selle perioodi pikkus mille kohta tahame arvutada iga keskmise ja mis algab aktsiahindade i-ndal kohal
        keskmine = round(harmonic_mean(periood), 6) # keskmise arvutamine ja ümardamine täpsuseni kuus kohta pärast koma
        keskmised.append(keskmine) #järjendi keskmised sisustamine keskmistega, mis on float tüüpi elemendid
    return(keskmised) # funktsioon tagastab ujukomaarvude järjendi, kuus kohta pärast koma
print(silu_andmed(failinimi, perioodi_pikkus))