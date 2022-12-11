kasutajanimi = input("Sisestage kasutajanimi: ")

def parool():
    global parool_1
    global parool_2
    parool_1 = input("Sisestage parool: ")
    parool_2 = input("Sisestage parool uuesti: ")
    return kontroll()

def kontroll(on_Taht=False,on_Number=False):
    if parool_1 != parool_2:
        print("Paroolid ei kattu!")
        parool()

    if len(parool_1) < 8:
        print("Parool peab olema pikem kui 7 märki.")
        parool()
     
    for i in range(len(parool_1)):
        if parool_1[i].isalpha():
            on_Taht = True
        if parool_1[i].isdigit():
            on_Number = True

    if on_Taht == False or on_Number == False:
        print("Parool peab sisaldama tähti ja numbreid.")
        parool()
    return parool_1[::-1]

f = open("users.txt","w")
f.write(kasutajanimi+":"+parool())
f.close()