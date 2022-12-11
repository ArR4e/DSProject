def p(parool):
    has_letter = False
    has_number = False
    for x in parool:
        if x.isalpha():
            has_letter = True
        elif x.isnumeric():
            has_number = True
        if has_letter and has_number:
            return True
    return False
nimi=input("Sisesta kasutajanimi:")

while True:
    parool=input("Sisesta parool:")
    uuesti=input("Sisesta parool uuesti:")
    if parool != uuesti:
        print("Paroolid ei klapi")
        continue
        
    if len(parool)<8:
        print("Parool peab olema vähemalt 8 tähemärki")
        continue
    
    if not p(parool):
        print("Paroolis peab olema nii tähti kui numbreid")
        continue
    break
        
parool=parool[::-1]
print(parool)

a=open("users.txt", "w")
a.write(nimi+":")
a.write(parool)
a.close()

        
    
    
    
    