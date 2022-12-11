def reverse(x):
    return x[::-1]
def parool():
    pwd1 = input("Sisestage parool: ")
    pwd2 = input("Kinnitage parool: ")
    alphabet = 0
    numeric = 0
    if pwd1 == pwd2:
        if len(pwd1) >= 8:
            for täht in pwd1:
                if täht.isalpha():
                    alphabet = 1
                elif täht.isnumeric():
                    numeric = 1
                else:
                    continue
            if alphabet == 1 and numeric == 1:
                y = reverse(pwd1)
                return y
            else:
                print("Paroolis peab kasutama nii tähti kui numbreid.")
                y = parool()
                return y
        else:
            print("Parool peab sisaldama vähemalt 8 tähemärki.")
            y = parool()
            return y
    else:
        print("Paroolid ei kattunud.")
        y = parool()
        return y
user = input("Sisestage kasutajanimi: ")
pwdout = parool()
file = open("users.txt", "w")
file.write(user + ":" + pwdout)
file.close()
