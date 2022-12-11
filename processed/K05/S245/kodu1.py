import re

kasutajanimi = input("Sisestage kasutaja nimi: ")
while True:
    
    parool1 = input("Sisestage esimene parool: ")
    parool2 = input("Sisestage teine parool: ")
    
    kehtiv = False
   
    if parool1 != parool2:
        print("Paroolid ei ühti!")
        continue
    elif (len(parool1)<8):
        print("Parool peab olema vähemalt 8 tähemärki pikk!")
        continue
    elif not re.search("[A-Z]",parool1):
        print("Parool peab sisaldama ühte suurt tähemärki!")
        continue
    elif not re.search("[a-z]",parool1):
        print("Parool peab sisaldama väikseid tähemärke!")
        continue
    elif not re.search("[1-9]",parool1):
        print("Parool peab sisaldama ühte numbrit!")
        continue
    else:
        kehtiv = True
        break

        
if(kehtiv):
    print("Parool sobib")


fail = open("users.txt", "w")
fail.write(kasutajanimi)
fail.write("\n")
fail.write(parool1[::-1])
fail.close()

    
    

    
