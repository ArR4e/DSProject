kasutajanimi = input("Sisesta kasutajanimi: ")        
while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    if parool1 != parool2:
        print("Sisesta sama parool!")
        False
    elif len(parool2) < 8:
        print("Sisesta parool, kus on vähemalt 8 tähemärki!")
        False
    elif not any(char.isdigit() for char in parool2):
        print("Sisesta numbreid sisaldav parool!")
        False
    else:
        break
    
f = open("users.txt", "x")
f.write(kasutajanimi + ":" + parool2 [::-1])
f.close()