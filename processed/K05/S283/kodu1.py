k_nimi = input("Kasutajanimi: ") #kasutajanimi küsitakse alguses ära, kuna selle valimisel kriteeriume ei ole

while True:
    parool = input("Parool: ") #kasutajalt küsitakse paroolid
    parool_k = input("Korrake parooli: ")
    if parool != parool_k: #programm kontrollib paroolide ühtivust
        print("Teie paroolid ei kattu, palun proovige uuesti.")
        continue #juhul kui parool ei sobi alustatakse uuesti parooli küsimisest
    if not len(parool) >= 8: #programm kontrollib, kas parool on 8 tähemärki pikk
        print("Teie parool peab olema vähemalt 8 tähemärki pikk.")
        continue #juhul kui parool ei sobi alustatakse uuesti parooli küsimisest
    number = 0 #muutujad mille abil programm tuvastab, kas parool sisastab nii tähti kui ka numbreid
    täht = 0
    for i in parool: #iga parooli sümbol vaadatakse üle
        if i.isnumeric(): #kui parooli sümbol on number siis lisatakse see numbrite muutujasse
            number += 1
        if i.isalpha(): #kui parooli sümbol on täht siis lisatakse see tähtede hulka
            täht += 1
    if not (täht > 0 and number > 0): #programm kontrollib, kas paroolis oli tähti või numbreid vaadates üle eelnevad muutujad
        print("Teie parool peab sisaldama nii tähti kui ka nubmreid.")
        continue #juhul kui parool ei sobi alustatakse uuesti parooli küsimisest
    else:
        break
    
krüpto_parool = parool[::-1] #parool keeratakse ümber

f = open("users.txt", "w+") #avatakse fail "users.txt" ja minnakse kirjutamise eesmärgiga

f.write(k_nimi +":") #faili kirjutatakse nimi ning koolon mis eraldab nime ja parooli(automaatkontroll nõudis nii)
f.write(krüpto_parool) #faili kirjutatakse parool

f.close()    
        

