def logimine(x, y):
    while x == y and len(x) > 7:
        if tjan(x) == True:
            continue
        else:
            print("parool ei sobi!")
            uuspass = input("Sisestage parool uuesti: ")
            uuspass2 = input("Korrake parooli: ")
            logimine(uuspass, uuspass2)
    
def tjan(y):
    return y.isalnum() and not y.isalpha() and not y.isdigit()
nimi = input("Sisestage kasutajanimi: ")
parool = input("Sisestage parool: ")
parool2 = input("Sisestage parool uuesti: ")
print(logimine(parool, parool2))

        