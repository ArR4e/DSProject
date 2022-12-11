kasutaja = input("Sisestage kasutajanimi:")
#parool = input("Sisestage parool:")
#parool2 = input("Sisestage parool teist korda:")

status = "algus"
file = open("users.txt", "w")

while True:
    if status == "algus":
        parool = input("Sisestage parool:")
        parool2 = input("Sisestage parool teist korda:")
        
        if parool == parool2:
            status = "taht"
        elif not parool == parool2:
            status = "algus"
            print("Paroolid ei kattu!")
            
    elif status == "taht":
        if len(parool) > 8:
            status = "nrjataht"
        else:
            status = "algus"
            print("Parool on liiga lühike!")
            
    elif status == "nrjataht":
        if parool.isalnum():
            status = "l6pp"
        elif parool.isalpha():
            status = "algus"
            print("Parool vajaks numbreid!")
        else:
            status = "algus"
            print("Parool vajaks tähti!")
            
    elif status == "l6pp":
        parool3 = parool[::-1]
        #file = open("users.txt", "w")
        with open("users.txt", "w") as file:
            file.write(f"kasutajanimi:{kasutaja}\nparool:{parool3}")
        break
            