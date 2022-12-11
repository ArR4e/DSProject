kn = input("Sisestage kasutajanimi: ")

def parool():
    password = input("Sisestage parool: ")
    password2 = input("Sisestage parool uuesti: ")
    if password != password2:
        print("Paroolid pole identsed!")
    if len(password) < 8:
        print("Tähemärki peab olema vähemalt 8!")
    if password.isalnum() == False:
        print("Parool peab sisaldama ka sümboleid!")
    if password.isalpha() == True:
        print("Parool peab sisaldama ka tähte!")
    a = kn
    b = password
    while password == password and len(password) >= 8 and password.isalnum() == True and password.isalpha() == True:
        file = open("users.txt", "w")
        file.write(a, b)
        file.close()
    
parool()