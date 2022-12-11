kn= input("Sisesta kasutajanimi: ")
while 1<2:
    p1= input("Sisesta parool esimest korda: ")
    p2= input("Sisesta parool teist korda: ")
    if p1==p2 and len(p1)>=8 and any(c.isdigit() for c in p1) ==True:
        p1=p1[::-1]
        fail=open("users.txt", "w")
        fail.write(kn + ":" + p1)
        fail.close()
        break
    elif p1!=p2: 
        print("Su paroolid pole ühtivad. Proovi uuesti.")
    elif len(p1)<8:
        print("Su parool pole vähemalt 8 tähemärki pikk. Proovi uuesti.")
    elif any(c.isdigit() for c in p1) !=True:
        print("Su parool ei sisalda numbreid. Proovi uuesti.")
        
        