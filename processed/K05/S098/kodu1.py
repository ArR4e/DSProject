kasutaja = input("Sisesta oma kasutajanimi: ")
tähestik = "qwertyuiopüõasdfghjklöäzxcvbnmðþ"
numbrid = "1234567890"
esimene = ""

def küsiparool():
    global esimene
    esimene = input("parool: ")
    teine = input("parool uuesti")
    
    if esimene  != teine:
        print("paroolid ei ühtinud")
        küsiparool()
    elif len(esimene) < 8:
        print("liiga lühike parool")
        küsiparool()
    elif not check(esimene):
        print("kasuta nii tähti kui ka numbreid")
        küsiparool()
    return True

def check(s):
    loe_tähed = 0
    loe_numbrid = 0
    for a in s:
        if a in tähestik: 
            loe_tähed = 1
        if a in numbrid:
            loe_numbrid = 1
        if loe_tähed and loe_numbrid:
            return True
        return False
tagurpid = ""
if küsiparool():
    for k in range(0, len(essa)):
        tagurpidi += essa[-1]
        essa = essa[:len(essa)-1]
with open("users.txt", "w") as fail:
    fail.write(f"{kasutaja}:{tagurpidi}\n")
         
    