file = open("users.txt", "w")
nimi = input("Sisesta kasutajanimi: ")
def numbridparoolis(parool):
    t=0
    n=0
    for i in parool:
        if i.isdigit():
            n = 1
        elif i.isalpha():
            t = 1
    if t == 1 and n == 1:
        return(True)
    else:
        return(False)

while True:
    pas = input("Sisesta parool: ")
    pas2 = input("Korda parooli: ")
    if pas2 != pas:
        print("Paroolid ei kattu")
    elif len(pas) < 8:
        print("Parool on vähem kui 8 tähemärki pikk")

    elif not numbridparoolis(pas):
        print("Parool peab sisaldama nii numbreid kui ka tähti")
    else:
        break
uusPas = ""
i = len(pas)
while i > 0:
    uusPas += pas[i-1]
    i-=1
file.write(nimi+":"+uusPas)
file.close()
        