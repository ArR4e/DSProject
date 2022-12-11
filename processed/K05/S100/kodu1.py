def numbersAndLetters(a):
    num = False
    let = False
    for i in a:
        if i.isdecimal():
            num = True
        elif i.isalpha():
            let = True
        if num and let:
            return True
    return False

def encryptAndWrite(a, b):
    f = open("users.txt", "w+")
    f.write(a + ":" + b[::-1])
    f.close()

kasutajanimi = input("Sisestage kasutajanimi: ")

while True:
    parool1 = input("Sisestage parool: ")
    parool2 = input("Kinnitage parool: ")
    
    if parool1 == parool2:
        if len(parool1) > 7:
            if numbersAndLetters(parool1):
                encryptAndWrite(kasutajanimi, parool1)
                break
            else:
                print("Paroolis ei leidu vähemalt ühte tähte ning ühte numbrit")
        else:
            print("Parool pole vähemalt 8 tähemärkki pikk")
    else:
        print("Paroolid ei kattu")
