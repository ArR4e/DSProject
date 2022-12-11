kn = input("Sisesta kasutajanimi: ")

def tjnr(a):
    return a.isalnum() and not a.isalpha() and not a.isdigit()

def tagurpidi(b):
    return b[::-1]

while True:
    p1 = str(input("Sisesta parool: "))
    p2 = str(input("Sisesta parool uuesti: "))
    if p1 == p2:
        if len(p2) >= 8:
            if tjnr(p2) == True:
                fp = tagurpidi(p2)
                w = open("users.txt", "w+")
                w.write(kn+":"+fp)
                w.close()
                break
            else:
                print("Parool peab sisaldama nii numbreid kui tähti.")
        else:
            print("Parool on liiga lühike.")
    else:
        print("Paroolid ei kattu.")
