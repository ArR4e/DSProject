kasutajanimi = input("Sisestage kasutajanimi: ")

while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool uuesti: ")
    def ühtivus(parool1, parool2):
        if parool1 == parool2:
            return True
        else:
            print("paroolid ei ühti")
            return False
    if ühtivus(parool1, parool2) != True:
        continue
    else:
        if not len(str(parool1)) >= 8:
            print("Parool peab olema minimaalselt 8 märki")
            continue
        else:
            def numbri_kontroll(parool1):
                return any(char.isdigit() for char in parool1)

            if numbri_kontroll(parool1) == False:
                print("Parool peab sisaldama numbreid")
                continue
            elif parool1.isdecimal() == True:
                print("Parool peab sisaldama tähti")
                continue
            else:
                break
            
def pööramine(parool1):
    return parool1[::-1]
t_parool = pööramine(parool1)
uus_kasutajanimi = t_parool

f = open("users.txt", "w")
f. write(str(kasutajanimi) + ":" + str(uus_kasutajanimi))
f. close()
