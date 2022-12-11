kasutajanimi = input("Kasutajanimi: ")

while True:
    parool1 = input("Parool: ")
    parool2 = input("Parool uuesti: ")
    
    if parool1 != parool2:
        print("Esimene parool ei kattu teise parooliga, proovi uuesti.")
        continue
    if len(parool1) < 8:
        print("Parool peab sisaldama vähemalt 8 tähemärki, proovi teist parooli.")
        continue
    if not any(char.isdigit() for char in parool1):
        print("Parool peab sisaldama nii tähti kui numbreid, proovi teist parooli.")
        continue
    
    if parool1 == parool2 and len(parool1) >= 8 and any(char.isdigit() for char in parool1):
        for char in range(len(parool1) - 1, -1, -1):
         print(parool1[char], end="")
        print("\n")
        
        f = open("users.txt", "w")
        f.write(str(kasutajanimi) + ":" + str(parool1))
        f.close()
        break
    
    