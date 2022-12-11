fail = open("users.txt", "a") #sest ma kirj sinna ja see jääb alles!!!
kasutajaNimi = input("Sisestage oma kasutajanimi: ")
tagurpidi = ""

while True:
    
    summa = 0
    tähed= 0
    arvud = 0
    parool1 = input("Sisestage oma parool: ")
    parool2 = input("Sisesatge oma parool uuesti: ")
    

    if parool2 != parool1:
        print ("Paroolid ei ole samad, proovige uuesti!")
        continue
    
    for tähtedeArv in parool2:
        summa +=1
        try:
            tähtedeArv = int(tähtedeArv)
        except:
            tähtedeArv = tähtedeArv
        if isinstance(tähtedeArv, int):
            arvud +=1
        if isinstance(tähtedeArv, str):
            tähed +=1
        
            
    if arvud == 0 or tähed == 0:
        print ("Salasõnas peavad olema nii tähed kui ka numbrid")
        continue
    
 
    if summa < 8:
        print("Parool liiga lühike, sisestage uus")
        continue
    
    break

while summa > 0:
    tagurpidi += parool2[summa - 1]
    summa -= 1
    
fail.write(kasutajaNimi + ":" + tagurpidi + "\n")

fail.close()

#print (tagurpidi)