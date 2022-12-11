def anydigits(parool):
    #будет возвращать тру или фалс, аргумент - строка, пароль.
    x = False
    for i in range (0, 10):
        if str(i) in parool:
            x = True
            break
    return x



def anyletters(parool):
    x = False
    for i in parool:
        if i.isalpha():
            x = True
            break
    return x 
    


username = input("Sisestage username: ")


while True:
    parool1 = input("Sisestage parooli esimest korda: ")
    parool2 = input("Sisestage parooli teist korda: ")
    if  parool1 != parool2:
        print(f"Esimene ja teine parool peavad olema samad, parooli pikkus vähemalt 8 tähte, parool peab siseldama vahemalt üks numbri.")
        continue
    if len(parool1) < 8:
        print(f"Esimene ja teine parool peavad olema samad, parooli pikkus vähemalt 8 tähte, parool peab siseldama vahemalt üks numbri.")
        continue
    if not(anydigits(parool1) and anyletters(parool1)):
        print(f"Esimene ja teine parool peavad olema samad, parooli pikkus vähemalt 8 tähte, parool peab siseldama vahemalt üks numbri.")
        continue
    break

print(parool1[::-1])
file = open("users.txt", "a")
file.write(username+":"+parool1[::-1]+"\n" )
file.close()
           
           
    
            


