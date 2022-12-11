f = open("users.txt", 'w')
kasutajanimi = input("Palun sisesta kasutajanimi: ")


while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    #kas paroolid kattuvad
    if not parool1 == parool2:
        print("Parool ei vasta nõuetele")
        continue
    #kontrollib parooli pikkust
    elif not (len(parool1) >=8):
        print("Parool ei vasta nõuetele")
        continue
    #kontrollib kas on olemas numbrid
    if not any(x.isdigit() for x in parool1) > 0:
        print("Parool ei vasta nõuetele")
        continue
    #keerab parooli tagurpidi
    tagurpidi = parool1[::-1]
    f.write(kasutajanimi + ":" + tagurpidi)
    break

f.close()