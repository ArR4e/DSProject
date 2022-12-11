def kysi_andmed():
    klapib = False

    nimi = input("Sisestage kasutajanimi: ")
    pass_1 = ""

    while not klapib:
        pass_1 = input("Sisestage parool: ")
        pass_2 = input("Sisestage parool uuesti: ")

        if pass_1 != pass_2:
            print("Paroolid ei klapi!")
            continue

        if len(pass_1) < 8:
            print("Parool peab olema vähemalt 8 tähemärki pikk!")
            continue

        if not any(t2ht.isdigit() for t2ht in pass_1) and \
           not any(t2ht.isdigit() for t2ht in pass_1):
            print("Parool peab sisaldama vähemalt ühte tähte ja ühte numbrit!")
            continue

        # Järelikult klapib
        break

    fail = open("users.txt", "a", encoding="utf-8")
    fail.write(nimi + ":" + pass_1[::-1] + "\n")
    fail.close()
    print("Parool salvestati edukalt!")

kysi_andmed()

