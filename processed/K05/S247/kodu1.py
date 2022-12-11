def leia_nr(n):
    x = "0123456789"
    for i in n:
        if i in x:
            return True
    return False
        
    
kasutajanimi=input("Sisestage kasutajanimi: ")
while True:
    parool1=input("Sisestage parool: ")
    parool2=input("Sisestage parool uuesti: ")
    
    if parool1!=parool2:
        print("Parool ei kattu ")
        continue
    elif len(parool1) < 8:
        print("Parool peab olema vähemalt 8 tähemärki pikk.")
        continue
    elif leia_nr(parool1) == False:
        print("Parool peab sisaldama numbrit")
        continue
    else:
        break
        
loorap = ""
for i in parool1:
    loorap = i + loorap
f = open("users.txt", "w")
f.write(str(kasutajanimi) + ":" + str(loorap))
f.close()
    
    