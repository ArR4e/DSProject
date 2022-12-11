kasutajanimi=str(input("Kasutajanimi: "))

def krüpt():
    loorap=str("")
    for i in parool:
        loorap=str(i)+loorap
    return loorap

def andmed():
    f=open("users.txt","w")
    f.write(kasutajanimi+":"+krüpt())
    f.close()

while True:
    parool=str(input("Parool: "))
    parool2=str(input("Parool uuesti: "))
    
    if parool2==parool and len(parool)>=8 and any(str.isdigit() for str in parool) and any(str.isalpha() for str in parool):
        break
    if parool2!=parool:
        print("Paroolid ei kattu")
    elif len(parool)<8:
        print("Parool peab olema vähemalt 8 tähemärki pikk")
    elif not any(str.isdigit() for str in parool):
        print("Parool peab sisaldama numbrit")
    else:
        print("Paroolis peab olema vähemalt üks täht")

andmed()

