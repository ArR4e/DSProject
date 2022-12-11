#Kontrollib kas sõnes on numbreid
def kas_numbreid(text):
    numbreid = False
    for char in text:
        if char.isdigit():
            numbreid = True
    return numbreid
#Kontrollib kas sõnes on tähti
def kas_tähti(text):
    tähti = False
    for char in text:
        if char.isalpha():
            tähti = True
    return tähti

nimi = input("Kasutajanimi: ")
while True:
    parool = input("Parool: ")
    parool2 = input("Parool: ")
    #Vaatab kas paroolid erinevad
    if parool != parool2:
        print("Sisestatud paroolid on erinevad.")
        continue
    #Vaatab kas parool väiksem kui 8 tähemärki
    elif len(parool) < 8:
        print("Parool peab olema vähemalt 8 tähemärki.")
        continue
    #Vaatab kas paroolis pole tähti või numbreid
    elif not kas_numbreid(parool) or not kas_tähti(parool):
        print("Parool peab sisaldama tähti ja numbreid.")
        continue
    break
#Keerab parooli tagurpidi
parool = parool[::-1]
#Kirjutab kasutajanime ja parooli faili users.txt
with open("users.txt","w") as file:
    file.write(nimi+":"+parool)