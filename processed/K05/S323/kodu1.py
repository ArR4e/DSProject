nimi = input("Sisestage kasutajanimi: ")
parool = input("Sisestage parool: ")
parool2 = input("Kinnitage parool: ")

def parooli_pööramine(parool):
    pööratud_parool = ""
    for täht in parool:
        pööratud_parool = täht + pööratud_parool
    return(pööratud_parool)

def numbrite_kontroll(parool):
    return any(char.isdigit() for char in parool)

def tähtede_kontroll(parool):
    return any(char.isalpha() for char in parool)

while parool != parool2:
    print("Parooli kinnitamisel tehti viga, sisestage uus parool.")
    parool = input("Sisestage parool: ")
    parrol2 = input("Kinnitage parool: ")

while len(parool) < 8:
    print("Paroolis peab olema vähemalt 8 tähemärki, sisestage uus parool.")
    parool = input("Sisestage parool: ")
    parrol2 = input("Kinnitage parool: ")
    
while numbrite_kontroll(parool) != True or tähtede_kontroll(parool) != True:
    print("Parool peab sisaldama nii tähti kui numbreid, sisestage uus parool.")
    parool = input("Sisestage parool: ")
    parrol2 = input("Kinnitage parool: ")
    
f = open("users.txt", "w")
f.write(nimi+ ":" + parooli_pööramine(parool))
f.close()