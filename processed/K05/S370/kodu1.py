def kattub(p, pk):
    if p ==pk:
        return True
    else:
        return False
    
def pikk(p):
    if len(p) >=8:
        return True
    else:
        return False
def tähed_ja_numbrid(p):
    if any(map(str.isdigit, p)) == True and any(map(str.isalpha, p)) == True:
        return True
    else:
        return False
    

nimi=input("Sisesta kasutajanimi: ")
while True:
    p=input("Sisesta parool: ")
    pk=input("Siseta parool kontrolliks uuesti: ")
    if kattub (p, pk) != True:
        print("Paroolid ei kattu")
    if pikk(p) != True:
        print("Parool ei ole pisiavalt pikk. Peab olema vähemalt 8 tähemärki.")
    if tähed_ja_numbrid(p) != True:
        print("Parool peab sisaldama nii tähti kui numbreid")
    if pikk(p) == True and tähed_ja_numbrid(p) == True and kattub(p, pk) == True:
        break
    print("Parool ei sobi. Tuleb valida uus parool.")
    
print("Parool sobib ning kirjutatakse koos kasutajanimega faili users.txt")
f= open("users.txt", "a")
f.write(nimi+":"+p[::-1])
f.close()
