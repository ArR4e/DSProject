import re

username = input("Sisestage kasutajanimi: ")
parool1 = input("Sisestage parool: ")
parool2 = input("Sisestage parool uuesti: ")

try:
    if parool1 == parool2:
        if len(parool1) > 7:
            if (re.match('^(?=.*\d)(?=.*[a-zA-Z])[\w~@#$%^&*+=`|{}:;!.?\"()\[\]-]', parool1)):
                f = open("users.txt", "w")
                f.write(username+":"+parool1[::-1])
                f.close()
                
            else:
                print("Parool peab sisaldama tahti ja numbreid")
        else:
            print("Parool on liiga luhike")
            
    else:
        print("Sisestatud paroolid ei ole samad")
except:
    print("Error something went wrong")