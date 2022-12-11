import re
nimi= input("Sisestage kasutajanimi : ")
for i in range (1):
    parool1= input("Sisestage oma parool: ")
    parool2= input("Sisestage oma parool: ")
    
    if parool1 != parool2:
        print("Teavita kasutajat puudusest")
        break
    if len(parool1)  < 8:
        print("Teavita kasutajat puudusest")
        break
    if len(parool2)  < 8:
        print("Teavita kasutajat puudusest")
        break
    elif re.search('[0,9]', parool1) is None:
        print("Teavita kasutajat puudusest")
        
    elif re.search('[0,9]', parool2) is None:
        print("Teavita kasutajat puudusest")
        
    parool= parool1=parool2
    pahupidi1= parool1[::-1]
    pahupidi2= parool2[::-1]
    f= open("users.txt", "w")
    f.write(f"Kasutajanimi: {nimi}")
    f.write(f"\nParool: {parool}")
    f.close()