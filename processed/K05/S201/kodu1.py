nimi = input("Sisesta oma kasutajanimi")
def parool():
    import re
    par1 = input("Sisesta uus parool")
    par2 = input("Sisesta uus parool")
    if par1 == par2:
        par1 = par2
    else:
        print("Sinu paroolid ei ühti")
        parool()
    if len(par1) <= 7:
        print("Sinu parool pole piisavalt pikk")
        parool()
    if not re.search("[0-9]", par1):
        print("Sinu parool peab sisaldama numbreid ja tähti")
        parool()
    if not re.search("[a-z]", par1):
        print("Sinu parool peab sisaldama numbreid ja tähti")
        parool()
    par1 = par1[::-1]
    print(par1)
    file = open("users.txt", "a") 
    file.write(nimi+":"+par1)
    file.close()
    
parool()

