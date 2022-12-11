#plokkskeem

file = open("users.txt", "w")

alpha = False
digit = False
passaccept = False
username = input("Sisesta kasutajanimi: ")

while not passaccept:
    upass = input("Sisesta parool: ")
    apass = input("Sisesta parool: ")
    if upass != apass:
        print("Paroolid ei ole samasugused. Proovi uuesti")
        continue
    
    elif len(upass) < 8:
        print("Parool on liiga lühike. Proovi uuesti")
        continue
    else:
        for char in upass:
            if char.isdigit():
                digit = True
            if char.isalpha():
                alpha = True
        if alpha and digit:
            passaccept = True
        else:
            print("Parool peab sisaldama numbreid ja tähti")
            continue
file.write(username + "." + upass[::-1])
file.close()