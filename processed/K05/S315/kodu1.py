import string
n = input("Sisesta kasutajanimi: ")
p = input("Sisesta parool: ")
p2 = input("Sisesta parool uuesti: ")

if p != p2:
    print("Paroolid ei ühildu")

    
elif p == p2:
    if len(p) < 8:
        print("Parool peab olema vähemalt 8 märki")

        
    else:
        for i in p:
            if i in string.punctuation:
                continue
            
            elif i.isalnum() == True:
                p3 = p[::-1]
                f = open("users.txt", 'a')
                f.write(n + ":" + p3)
                f.close()
                break

            elif i.isalnum() == False:
                print("Kasuta tähti ja numbreid")

    
                