def tahjanum(parool):
    tah = False
    num = False
    for i in parool:
        if i.isalpha() == True:
            tah = True
        if i.isnumeric() == True:
            num = True
    if tah == True and num == True:
        return True
    else:
        return False

login = input("Sisesta kasutajanimi: ")
while True:
    parool1 = input("Sisesta parool: ")
    parool2 = input("Sisesta parool veelkord: ")
    if parool1 == parool2:
        if len(parool1) >= 8:
            if tahjanum(parool1)  == True:
                break
    print("Parool ei vasta nõutele. Proovi uuesti.")

t_parool = parool1 [::-1]
db = open("users.txt", "a")
db.write(login + ":" + t_parool)
db.close()