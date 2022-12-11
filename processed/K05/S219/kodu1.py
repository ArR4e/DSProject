def numberparoolis(x):
    if True in [parool1.isdigit() for parool1 in x]:
        return True
    return False

kasutajanimi = input("Sisesta kasutajanimi: ")
parool1 = input("Sisesta parool: ")
parool2 = input("Sisesta parool uuesti: ")

while parool1 != parool2:
    print("Kahel korral sisestatud paroolid ei kattu.")
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    
while len(parool1) < 8:
    print("Parool peab olema vähemalt 8 tähemärki pikk.")
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    
while numberparoolis(parool1) == False:
    print("Parool peab sisaldama numbreid.")
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    
while parool1.islower() or parool1.isupper() == False:
    print("Parool peab sisaldama tähti.")
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    
uusparool = parool1[::-1]

f = open("users.txt", "w")
f.write(str(kasutajanimi) + ":" + str(uusparool))
f.close()