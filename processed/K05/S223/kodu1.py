def singUp(username, password):
    password = password[::-1]
    return str(username) + ":" + str(password)

nimi = input("Sisesta kasutajanimi: ")

while True:
    list_numbrid = [1,2,3,4,5,6,7,8,9,0]
    password = []
    password += [str(input("Sisesta parool: "))]
    password += [str(input("Sisesta parool: "))]
    if password[0] != password[1]:
        print("Parooli kinnitamine ebaõnnestus, proovi uuesti")
    elif len(password[0]) < 8:
        print("Parool ei olnud vähemalt 8 tähemärki pikk")
    elif [x for x in list_numbrid if str(x) in password[0]] == []:
        print("Paroolis peavad olema nii tähed kui numbrid")
    else:
        break

def uusFail(kood):
    fail = open("users.txt", "w+")
    fail.write(kood)
    fail.close()

uusFail(singUp(nimi, password[0]))