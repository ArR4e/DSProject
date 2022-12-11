# 1. Plokkskeem
# Järgmisel plokkskeemil on kujutatud ühe veebilehe registreerimisvormi algoritm.
# Kirjuta programm, mis realiseerib plokkskeemil kirjeldatu.

user = input("Kasutajanimi: ")

while True:
    pass1 = input("Sisesta parool (vähemalt 8 tähemärki): ")
    pass2 = input("Sisesta parool veel kord: ")
    if pass1 != pass2:
        print("Paroolid ei kattu.")
        continue
    else:
        if len(pass1) < 8:
            print("Paroolil peab olema vähemalt 8 tähemärki.")
            continue
        else:
            count_str = 0
            count_int = 0
            for tähemärk in pass1:
                try:
                    a = int(tähemärk)
                    count_int += 1
                except:
                    a = str(tähemärk)
                    count_str += 1
            
            if count_str < 1 or count_int < 1:
                print("Parool peab sisaldama tähti ja numbreid.")
                continue
            else:
                pass_bw = pass1[::-1]
                user_pwd_bw = str(user + ":" + pass_bw)
                f = open("users.txt", "w")
                f.write(user_pwd_bw)
                f.close()
                break
                    