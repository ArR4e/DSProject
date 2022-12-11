nimi = input("Nimi: ")
while True:
    parool1 = input("Parool: ")
    parool2 = input("Parool: ")
    if parool1 == parool2:
        if len(parool1) >= 8:
            letter = False
            num = False
            
            for i in parool1:
                if i.isalpha():
                    letter = True
                if i.isdigit():
                    num = True
            
            if letter and num:
                file = open("users.txt", "w")
                file.write(nimi + ":" + parool1[::-1])
                file.close()
                break
                    
            else:
                print("Parool peab kasutama nii tähti kui numbreid. Proovige uuesti")
            continue
            
        else:
            print("Parool peab olema vähemalt 8 tähemärki pikk. Proovige uuesti")
        continue
            
    else:
        print("Esimene parool ei kattu teise parooliga. Proovige uuesti")
    continue