import re
nimi = input("Sisestage kasutajanimi: ")

def õigeparool():
    while True:
        parool = input("Sisestage parool: ")
        parool2 = input("Sisestage parool uuesti: ")
        if parool != parool2:
            print("Sisestasite vale parooli")
        if len(parool) < 8:
            print("Sisestasite vale parooli")
        elif re.search('[0-9]',parool) is None:
            print("Sisestasite vale parooli")
        else:
            break
        
    f = open("users.txt", "w")
    f.write(nimi+":"+ parool[::-1])
    f.close()

õigeparool()


