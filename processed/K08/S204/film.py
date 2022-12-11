a=str(input("Sisesta filmi žanri nimi: "))

def loetleFilmid(a):
    fail = open("filmid.txt", encoding="UTF-8")
    while True:
        
        b=fail.readline().strip()
        c=fail.readline().strip()
        d=fail.readline().strip()
        e=fail.readline().strip()
        f=fail.readline().strip()
        l=fail.readline().strip()
    
        break
    
    g=b.split("- ")
    h=c.split("- ")
    i=d.split("- ")
    j=e.split("- ")
    k=f.split("- ")
    m=l.split("- ")
    järjend=[]    
    while True: 
        if str(a) == g[1]:
            järjend=järjend+[g[0]]
        
        if str(a) == h[1]:
            järjend=järjend+[h[0]]
        
        if str(a) == i[1]:
            järjend=järjend+[i[0]]
        
        if str(a) == j[1]:
            järjend=järjend+[j[0]]
        
        if str(a) == k[1]:
            järjend=järjend+[k[0]]
        
        if str(a) == m[1]:
            järjend=järjend+[m[0]]
        break
    return(järjend)
    
    
    
    fail.close()
print(loetleFilmid(a))

x=str(input("Sisesta filmi nimi: "))
z=str(input("Sisesta lisatud filmi žanri nimi: "))
#Halb lahendus, sest töötab vaid 6 filmiga.
def lisaFilm(x, z):
    fail = open("filmid.txt", "a", encoding="UTF-8")
    y=(str(x)+ " - "+str(z))
    
    
    fail.write("\n")        
    return fail.write(y)
    
    fail.close()
lisaFilm(x, z)
o=str(input("Sisesta mingi filmi nimi, et see ära kustutada: "))
def kustutaFilm(o):
    fail = open("filmid.txt", "r", encoding="UTF-8")
    lines=fail.readlines()
    for rida in lines:
        ai = rida.split(" - ")
        if ai[0]==o:
            rida=("\n")
    return lines    
    fail.close()
kustutaFilm(o)
