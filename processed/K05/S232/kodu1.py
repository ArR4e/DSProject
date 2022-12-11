def on_number(a):
    for element in a:
        if element.isdigit():
            return True
    return False

file = open("users.txt", "w+")

kasutajanimi = input("Palun sisesta kasutajanimi: ")
parool1 = input("Palun sisesta parool esimest korda: ")
parool2 = input("Palun sisesta parool teist korda: ")
algusesse = "Viga! Pöördu algusesse. Paroolil on puuduseks, et "

if parool1 == parool2:
    if len(parool1) >= 8:
        if on_number(parool1):
            loorap = parool1[::-1]
            file.write(kasutajanimi + ":" + loorap)
            print("Kasutajanimi ja parool on salvestatud!")
        else:
            print(algusesse + "parool peab sisaldama tähti ja numbreid!")
    else:
        print(algusesse + "parooli pikkus peab olema 8 tähemärki.")
else:
    print(algusesse + "paroolid ei klapi.")
    
file.close()