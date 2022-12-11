def paroolide_kattumine(parool_1,parool_2):
    if parool_1 == parool_2:
        return True
    else:
        return False

def parooli_pikkus(parool):
    if len(parool) >= 8:
        return True
    else:
        return False

def tähe_kontroll(parool):
    for i in parool:
        if i.isalpha():
            return True
    return False

def numbri_kontroll(parool):
    for i in parool:
        if i.isdigit():
            return True
    return False
def muu_kontroll(parool):
    for i in parool:
        if i.isdigit()==False and i.isalpha()==False:
            return False
        else:
            return True

def krüpto(parool):#sain siit abi https://www.geeksforgeeks.org/reverse-string-python-5-different-ways/
    str = ""
    for i in parool:
        str = i + str
    return str

kasutajanimi = input("Kasutajanimi: ")
while True:
    parool_1 = input("Parool: ")
    parool_2 = input("Parool uuesti: ")
    if paroolide_kattumine(parool_1,parool_2) == True:
        if parooli_pikkus(parool_1) == True:
            if tähe_kontroll(parool_1) == True and numbri_kontroll(parool_1) == True and muu_kontroll(parool_1)== True:
                f = open("users.txt", "w")
                f.write(kasutajanimi+":"+krüpto(parool_1))
                f.close()
                break
            else:
                print("Parool peab sisaldama tähti ja numbreid!")
        else:
            print("Parool peab sisaldama vähemalt 8 tähemärki!")
    else:
        print("Paroolid ei kattu!")
