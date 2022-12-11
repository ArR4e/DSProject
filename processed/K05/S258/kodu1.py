nimi=input("Sisesta kasutajanimi: ")
pass1=""
pass2=""

def password_maker():
    global pass1
    global pass2
    pass1=input("Sisesta parool: ")
    pass2=input("Korda parooli: ")
    return pass1==pass2

def password_lengther():
    global pass1
    return len(pass1)>=8

def password_letterer():
    global pass1
    mega=False
    megaga=False
    for i in pass1:
        if i in "0123456789":
            mega=True
    for i in pass1:
        if i in "qwertyuiopüõasdfghjklöäzxcvbnmQWERTYUIOPÜÕASDFGHJKLÖÄZXCVBNM":
            megaga=True
    return mega and megaga

printer=open("users.txt","w")

while True:
    if not password_maker():
        print("Paroolid ei klapi, proovi uuesti!")
    elif not password_lengther():
        print("Parool pole piisavalt pikk (min. 8 tähemärki), proovi uuesti!")
    elif not password_letterer():
        print("Parool peab sisaldama vähemalt ühet tähet ja numbrit, proovi uuesti!")
    else:
        pass2=""
        for i in range(1,len(pass1)+1):
            pass2 +=pass1[-1*i]
        printer.write(nimi+":"+pass2)
        break
printer.close()