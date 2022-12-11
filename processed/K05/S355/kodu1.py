username = input("Sisesta kasutajanimi: ")

while True:
    
    pass1 = input("Sisesta parool: ")
    pass2 = input("Sisesta parool uuesti: ")
    passcount = len(pass1)
    


    if pass1 == pass2:
        if passcount >= 8:
            if pass1.isdecimal():
                print("Paroolis peab leiduma ka tähti")
            elif pass1.isalpha():
                print("Paroolis peab leiduma ka numbreid")
            else:
                passcrypt = pass1[::-1]
                print("Encrypted password is", passcrypt)
                break
        else:
            print("Parooli pikkus peab olema vähemalt 8 tähemärki")
    else:
        print("See 2. korral sisestatud parool ei kattunud 1. korral sisestatud parooliga.")

f = open("users.txt", "w")
f.write(username + ":" + passcrypt)
f.close()
            
        