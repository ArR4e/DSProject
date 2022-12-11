import re
def askPwd():
    global pwd1
    pwd1=input("Sisesta parool: ")
    global pwd2
    pwd2=input("Sisesta parool teist korda: ")
    checkPwd1()

def checkPwd1():
    if pwd1==pwd2:
        checkPwd2()
    else:
        print("Paroolid ei kattu")
        askPwd()

def checkPwd2():
    while True:
        is_valid = False
        
        if len(pwd2)<8:
            print("Parool peab olem vähemalt 8 tähemärki pikk.")
            askPwd()
            continue
        elif not re.search("[a-z]",pwd2):
            print("Parool peab sisaldama tähti.")
            askPwd()
            continue
        elif not re.search("[1-9]",pwd2):
            print("Parool peab sisaldama numbreid.")
            askPwd()
            continue
        else:
            is_valid = True
            break
        login()

def login():
    dwp=(pwd2 [::-1])
    f=open("users.txt", "w")
    f.write(str(usr))
    f.write(":")
    f.write(dwp)
    f.close()

usr=input("Sisesta kasutajanimi: ")
askPwd()
checkPwd1()
checkPwd2()
login()
print("Kasutajanimi ja parool on salvestatud.")
