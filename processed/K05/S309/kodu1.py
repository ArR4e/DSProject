#abimeetodid
def containsdigit(string):
    return any(char.isdigit() for char in string)

def containschar(string):
    return any(char.isalpha() for char in string)

def reversestring(string):
    return string[::-1]

#muutujad
username = str(input("Sisestage kasutajanimi: "))
pwd1 = ""
pwd2 = ""
#peamine tsükkel
while(True):
    #küsime paroole
    pwd1 = str(input("Sisestage parool: "))
    pwd2 = str(input("Sisestage parool uuesti: "))

    if(not(pwd1 == pwd2)):
        print("Paroolid ei kattunud, proovige uuesti.")
        continue

    if(not(len(pwd1) >= 8)):
        print("Parool peab olema vähemalt 8 tähemärki, proovige uuesti")
        continue
    
    if(not(containsdigit(pwd1) and containschar(pwd1))):
        print("Parool peab sisaldama vähemalt ühte tähemärki ja ühte numbrit, proovige uuesti.")
        continue
    
    break

#kirjutame failile, kustutades sealt muu olemasoleva
file = open("users.txt", "w")
file.write((username + ":" + reversestring(pwd1)))
file.close()
