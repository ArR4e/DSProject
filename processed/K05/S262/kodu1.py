def numbridtahed(n):
    nr = 0
    tahed = 0
    for mark in n:
        if mark.isalpha() == True:
            tahed += 1
        if mark.isnumeric() == True:
            nr += 1
    if nr > 0 and tahed > 0:
        return True
    else:
        return False
def kontroll(x,y):
    if x != y:
        print("Paroolid ei kattu.")
        return False
    if len(x) < 8:
        print("Parool on lühem kui 8 märki.")
        return False
    if numbridtahed(x) == False:
        print("Paroolis ei ole kasutatud tähti ja numbreid.")
        return False
    else:
        return True
    

kasutajanimi = input("Sisestage kasutajanimi: ")
parool1= input("Sisestage parool: ")
parool2 = input("Sisestage parool uuesti: ")
parooltagurpidi = ""
while True:
    if kontroll(parool1,parool2) == True:
        break
    else:
        parool1= input("Sisestage parool uuesti: ")
        parool2 = input("Sisestage parool veel kord: ")
    
marke = len(parool1)
while marke > 0:
    parooltagurpidi += parool1[marke-1]
    marke -= 1

f= open("users.txt","w+",encoding="UTF-8")
f.write(kasutajanimi + ":" + parooltagurpidi)
f.close()
