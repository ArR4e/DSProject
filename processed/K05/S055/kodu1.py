nimi = input("kasutajanimi: ")

def t2hed_ja_numbrid(s6ne):
    numbrid = False
    t2hed = False
    for t2ht in s6ne:
        if t2ht.isdigit():
            numbrid = True
        elif t2ht.isalpha():
            t2hed = True
    return numbrid and t2hed

while True:
    parool = input("Sisesta parool: ")
    parool2 = input("Korda parooli: ")
    if parool != parool2:
        print("Pole samad")
        continue
    elif len(parool) < 8:
        print("Liiga lyhike")
        continue
    elif not t2hed_ja_numbrid(parool):
        print("Peab sisaldama t2hti ja numbrid")
        continue
    else:
        f = open("users.txt", "w")
        f.write(nimi + ":" + parool[::-1])
        f.close()
        break
