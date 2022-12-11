import string

kasutajanimi = input("Sisestage kasutajanimi: ")

while True:
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage parool uuesti: ")
    
    tähed = False
    numbrid = False
    
    if parool1 != parool2 or len(parool1) < 8:
        print("Parool on vigane!")
        continue
    else:
        for tähemärk in parool1:
            if tähemärk in string.ascii_letters:
                tähed = True
            if tähemärk in string.digits:
                numbrid = True
        
        if tähed and numbrid:
            break
        continue

parool1 = parool1[::-1]

fail = open("users.txt","w", encoding="UTF-8")         
fail.write(f"{kasutajanimi}:{parool1}")
fail.close()


    
   
            