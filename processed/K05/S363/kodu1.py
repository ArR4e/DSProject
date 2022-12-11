f = open("users.txt","w")

kasutaja = input("Palun vali endale kasutajanimi: ")


number = 0
täht = 0
a = 0

while a==0:
    parool = input("Palun vali endale parool: ")
    kordus = input("Palun korda enda parooli: ")
    
    #kas on sama
    if parool == kordus:
        parool = list(parool)
        
        #kas on piisavalt pikk
        if len(parool) >= 8:
            for i in parool:
                if i.isalpha():
                    täht += 1
                if i.isnumeric():
                    number += 1
            
            #kas on tähed ja numbrid
            if number>0 and täht>0:
                parool.reverse()
                parool = "".join(parool)
                f.write(kasutaja+":"+parool)
                a = 1
            
            elif number>0 and täht == 0:
                print("Parooli peab sisaldama tähti")
                continue
            
            elif number == 0 and täht>0:
                print("Parool peab sisaldama numbreid")
                continue
            
            else:
                print("Parool peab sisaldama tähti ja numbreid")
                continue
                    
        else:
            print("Parool peab olema vähemalt 8 tähemärki pikk")
            continue
                
    else:
        print("Paroolid ei kattu")
        continue
            
f.close()
