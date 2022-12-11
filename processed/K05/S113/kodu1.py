kasutajanimi = str(input("Palun sisesta oma kasutajanimi:"))
def paroolid():
    global a
    global b
    a = input("Sisestage parool: ")
    b = input("Sisestage parool korra veel: ")
    return [a, b]
def samad():
    if a == b:
        return True
    else:
        print("Paroolid ei ühti!")
        return False
def pikk():
    if len(a) >= 8:
        return True
    else:
        print("Parool on liiga lühikene!")
        return False
def tähjanr():
    if a.isalpha() == False and a.isnumeric() == False:
        return True
    else:
        print("Paroolis pole nii tähti kui ka numbreid")
        return False
def plokkskeem():
    while True:
        paroolid()
        if samad() == False:
            continue
        if pikk() == False:
            continue
        if tähjanr() == False:
            continue
        else:
            print("Parool on OK!")
            break
def lõpp():
    pikkus = len(a)
    tagurpidi = a[pikkus::-1]
    fail = open("users.txt", "w")
    fail.write(kasutajanimi)
    fail.write(":")
    fail.write(tagurpidi)
    fail.close()
    
plokkskeem()
lõpp()