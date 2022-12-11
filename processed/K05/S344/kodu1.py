kasutajanimi = input("Sisesta Enda kasutajanimi: ")
parool_1 = input("Sisesta parool: ")
parool_2 = input("Sisesta teistkorda parool: ")

def kattuvus(parool_1, parool_2):
    while True:
        if parool_1 != parool_2:
            print("Paroolid ei kattu omavahel!")
            parool_1 = str(input("Sisesta parool: "))
            parool_2 = str(input("Sisesta teistkorda parool: "))
        else:
            break

def tähemärk(parool_1):
    while True:
        if len(parool_1) < 8:
            print("Paroolid ei olnud kaheksa tähemärki!")
            parool_1 = str(input("Sisesta parool: "))
            parool_2 = str(input("Sisesta teistkorda parool: "))
        else:
            break
        
def tähed_numbrid(parool_1):
    while True:
        if tähed(parool_1) == False :
            print("Paroolid ei olnud numbreid!")
            parool_1 = str(input("Sisesta parool: "))
            parool_2 = str(input("Sisesta teistkorda parool: "))
        elif numbrid(parool_1) == False:
            print("Paroolid ei olnud tähti")
            parool_1 = str(input("Sisesta parool: "))
            parool_2 = str(input("Sisesta teistkorda parool: "))
        else:
            break
        
def tähed(parool_1):
    return any (parool.isdigit() for parool in parool_1)
def numbrid(parool_1):
    return any (parool.isalpha() for parool in parool_1)

def rotate(parool_1):
    n = len(parool_1)
    pööre = ""
    while n > 0:
        pööre = pööre + parool_1 [n - 1: n]
        n -= 1
    return pööre
    

kattuvus(parool_1, parool_2)
tähemärk(parool_1)
tähed_numbrid(parool_1)


f = open("users.txt", "w+")
f.write(kasutajanimi)
f.write(":")
f.write(rotate(parool_1))
f.close()
