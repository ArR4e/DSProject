import re

x = input("Sisesta kasutajanimi: ")

def parool():
    
    while True:
        y = input("Sisesta parool: ")
        z = input("Sisesta parool teist korda: ")
        if not y == z:
            print("Paroolid ei kattu, proovi uuesti.")
        
        elif len(z) < 8:
            print("Parool peaks olema vähemalt 8 ühikut pikk.")
            
        elif not re.search("[0-9]" , z):
            print("Parool peaks sisaldama numbrit.")
            
        if y == z:
            with open('users.txt', 'w') as f:
            e = z[::-1]
            f.write(x+":"+e)
            f.close()
            break
            
        

            
    
             




