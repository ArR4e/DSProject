kasutajanimi = input("Sisestage kasutajanimi: ")
while True:
        parool1 = input("Sisestage parool: ")
        parool2 = input("Sisestage parool veel kord: ")
        if parool1 == parool2 and len(parool1) == 8 and parool1.isalpha() != True and parool1.isnumeric() != True:
            print("Tubli!")
            break
        else:
            print("Proovi uuesti!")
            continue
parooltagurpidi = ""
for i in range(len(parool1)-1, -1, -1):
    parooltagurpidi += parool1[i]
print(parooltagurpidi)
fail = open("users.txt", "w")
fail.write(kasutajanimi + ":" + parooltagurpidi)
fail.close()