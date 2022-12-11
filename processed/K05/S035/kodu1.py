def numbrid(sisend):
    return any(char.isdigit() for char in sisend)
def tähed (sisend):
    return any(char.isalpha() for char in sisend)
kasutajanimi=str(input("Sisesta kasutajanimi: "))
parool=str(input("Sisesta parool: "))
parool2=str(input("Kinnita parool: "))
while True:
    if parool==parool2 and len(parool)>=8 and numbrid(parool)==True and tähed(parool)==True:
         parool=parool[ : :-1]
         break
    elif parool != parool2 :
        print("Sisestatud paroolid pole samad!")
        parool=str(input("Sisesta parool: "))
        parool2=str(input("Kinnita parool: "))
        continue
    elif len(parool)<8:
        print("Parool on lühem kui 8 märki!")
        parool=str(input("Sisesta parool: "))
        parool2=str(input("Kinnita parool: "))
        continue
    elif numbrid(parool)==False:
        print("Parool peab sisaldama vähemalt ühte numbrit!")
        parool=str(input("Sisesta parool: "))
        parool2=str(input("Kinnita parool: "))
        continue
    elif tähed(parool)==False:
        print("Parool peab sisaldama vähemalt ühte tähte!")
        parool=str(input("Sisesta parool: "))
        parool2=str(input("Kinnita parool: "))
        continue
f = open("users.txt", "w")
f.write(kasutajanimi + ":" + parool)
f.close()
