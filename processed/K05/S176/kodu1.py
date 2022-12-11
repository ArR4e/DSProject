print("Tere, palun looge kasutaja.")

def sisaldus(parool):
    for tähemärki in parool:
        if tähemärki.isdigit():
            return True
    return False
kasutajanimi = input("Sisestage kasutajanimi: ")
while True:
    try:
        parool = input("Sisestage parool: ")
        parool2 = input("Sisestage parool uuesti: ")
    except:        
        continue
    if parool != parool2:
        print("Paroolid ei kattu!")
    elif len(parool) < 8:
        print("Parool on liiga lühike!")
    elif sisaldus(parool) == False:
        print("Parool ei sisalda numbreid!")
    else:
        break
def kasutaja(kasutajanimi, parool):
        parool = parool[::-1]
        f = open("users.txt", "w")
        f.write(kasutajanimi)
        f.write(":")
        f.write(parool)
        f.close
kasutaja(kasutajanimi, parool)
print("Kasutaja loodud!")