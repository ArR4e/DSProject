kasutajanimi = str(input("Sisesta kasutajanimi:"))
parool_1 = str(input("Sisesta parool:"))
parool_2 = str(input("Sisesta parool uuesti:"))

# if not parool_1 == parool_2:
#     print("Paroolid ei kattu.")


while True:
    if parool_1 != parool_2:
        print("Paroolid ei klapi.")
        parool_1 = str(input("Sisesta parool:"))
        parool_2 = str(input("Sisesta parool uuesti:"))

    if not len(parool_1) > 7:
        print("Parool peab olema vähemalt 8 tähemärki pikk.")
        parool_1 = str(input("Sisesta parool:"))
        parool_2 = str(input("Sisesta parool uuesti:"))
    
    else:
        break


tagurpidi = parool_1[::-1]

f = open("users.txt", "w")
f.write(kasutajanimi + ":" + tagurpidi)
f.close()
