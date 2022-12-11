nimi = input("Sisesta oma kasutajanimi: ")
parool1 = input("Sisesta parool: ")
parool2 = input("Sisesta parool uuesti: ")

if parool1 == parool2:
    print("Paroolid kattuvad.")
else:
    print("Paroolid ei ühti.")

if len(parool2) >= 8:
    print("Parool piisavalt pikk.")
else:
    print("Parool peab olema vähemalt 8 tähemärki.")

