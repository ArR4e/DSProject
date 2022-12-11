kas1 = input("Sisestage oma kasutajanimi: ")
pas1 = input("Sisestage oma parool: ")
pas2 = input("Sisestage oma parool teist korda: ")

def kontroll(pas1, pas2):
    sisaldab = False
    sisaldab2 = False

    for sõna in pas2:
        if sõna.isdigit():
            sisaldab = True
            
    for sõna in pas2:
        if sõna.isalpha():
            sisaldab2 = True
            
    return sisaldab and sisaldab2

while True:
    try:
        x = len(str(pas2))
        if pas2 == pas1 and x >= 8 and kontroll(pas1, pas2) == True:
            f = open("users.txt", "w")
            f.write(kas1 + ":" + pas2[::-1])
            f.close()
            break
        else:
            print("Parool ei sobi")
            pas1 = input("Sisestage oma parool uuesti: ")
            pas2 = input("Sisestage oma parool teist korda: ")
    except:
        break
        
