def paroolikontroll(parool1,parool2):
    #kaks parooli kattuvad
    if parool1!=parool2:
        return False
    #Parooli pikkus vähemalt 8 märki
    if len(parool1)<8:
        return False
    #Parool sisaldab numbreid ja tähti
    tyyp=False
    vajalik_nr=["0","1","2","3","4","5","6","7","8","9"]
    numbrid=0
    tahed=0
    for i in range(len(parool1)):
        if parool1[i] in vajalik_nr:
            tyyp=True
        if tyyp==True:
            numbrid+=1
            tyyp=False
        else:
            tahed+=1
    if numbrid==0 or tahed==0:
        return False
    return True

def pooraringi(parool):
    uus_parool=""
    n=len(parool)
    for i in range(len(parool)):
        uus_parool=uus_parool+parool[n-i-1]
    return uus_parool    


kasutajanimi=input("Palun sisesta kasutajanimi: ")
kontroll=False

while kontroll!=True:
    parool1=input("Palun sisesta oma parool: ")
    parool2=input("Palun sisesta oma parool uuesti: ")
    kontroll=paroolikontroll(parool1,parool2)

pooratud_parool=pooraringi(parool1)
kasutajale=kasutajanimi+":"+pooratud_parool

filename="users.txt"
fail1=open(filename,"w")
fail1=open(filename,"a")
fail1.write(str(kasutajale))
fail1.close()
