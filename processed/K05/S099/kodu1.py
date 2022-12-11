kasutaja = input("Sisesta kasutajanimi: ")
f = open("users.txt", "w")

def on_number(parool):
    for number in parool:
        if number.isdigit():
            return True
    
def on_t2ht(parool):
    for t2ht in parool:
        if t2ht.isalpha():
            return True

def tagurpidi(pw):
    i = len(pw)
    parool = ""
    while i > 0:
        parool += pw[i-1]
        i -= 1
    return parool
    
def parool():
    while True:
        p1 = input("Sisesta parool esimest korda: ")
        p2 = input("Sisesta parool teist korda: ")
        if p1 != p2:
            print("Paroolid ei kattu, proovi uuesti!")
        elif len(p1) >= 8:
            if on_t2ht(p1) and on_number(p1):
                return tagurpidi(p1)
                break
            else:
                print("Parool peab sisaldama vähemalt üht numbrit ja tähemärki!")
        else:
            print("Parool peab olema vähemalt 8 tähemärki pikk!")
parool = str(parool())

print(kasutaja + ":" + parool)
f.write(kasutaja + ":" + parool)
f.close()