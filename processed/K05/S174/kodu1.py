kasutajanimi = input("Palun sisesta oma kasutajanimi: ")

#https://stackoverflow.com/questions/18871841/how-to-reverse-words-in-python
#sain sõne ümberpööramise abi siit
while True:
    parool1 = input("Sisesta oma parool esimest korda: ")
    parool2 = input("Sisesta oma parool teist korda: ")
    if parool1 == parool2:
        if len(parool1) >= 8:
            if not parool1.isalpha() and not parool1.isnumeric():
                tagurpidiparool = parool1[::-1]
                f = open("users.txt", "w")
                f.write(kasutajanimi + ":" + tagurpidiparool)
                f.close()
                break
            else:
                print("Vigane parool! Parool peab koosnema tähtedest ja numbritest.")
        else:
            print("Parool peab olema 8 tähemärki.")
    else:
        print("Paroolid ei kattu.")
            