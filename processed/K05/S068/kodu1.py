def pööre(a):
    return a[::-1]

nimi=str(input("Sisestage kasutajanimi: "))
while True:
    parool1=str(input("Sisestage parool:"))
    parool2=str(input("Sisestage parool uuesti:"))
    if parool1==parool2:
        len(parool1) >=8
        any(a.isalpha() for a in parool1)
        any(a.isupper()for a in parool1)
        any(a.isdigit()for a in parool1)
        any(not a.isalnum()for a in parool1)
        f=open("users.txt","a", encoding="UTF-8")
        f.write(nimi + ":" +str(pööre(parool1)))
        f.close()
        break
        
