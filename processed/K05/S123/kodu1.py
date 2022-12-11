kasutajanimi=input("Sisesta kasutajanimi: ")
    
def paroolidkontroll():
    while True:
        parool1=input("Sisesta parool 1. korda: ")
        parool2=input("Sisesta parool 2. korda: ")
        
        if parool1!=parool2:
            print("paroolid ei kattu")
            continue
        
        if len(parool1)<8:
            print("liiga lühike")
            continue
        
        if not parool1.isnumeric() and not parool1.isalnum() and not parool1.isprintable():
            print("ei sisalda tähti ega numbreid")
            continue
        tagurpidi=parool1[::-1]
        
        fail=open('users.txt', 'w')
        fail.write(kasutajanimi+":"+tagurpidi)
        fail.close()
        
        break
            

paroolidkontroll()