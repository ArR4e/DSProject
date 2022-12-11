un=input("Kasutajanimi: ")

def paroolimajandus():
    while True:
    
    
        pw1=input("Parool: ")
        pw2=input("Korda parooli : ")
        if not pw1==pw2:
            print("Paroolid ei kattu")
            continue
        if not len(pw1)>=8:
            print("Parool on liiga lühike")
            continue
        if not pw1.isalnum() and not pw1.isprintable():
            print("Paroolis pole numbreid või tähti")
            continue
        
        pw1 = pw1[::-1]
        f = open("users.txt", "w")
        f.write(un + ":" + pw1)
        f.close()
        break
paroolimajandus()
        
