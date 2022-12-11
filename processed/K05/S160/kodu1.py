import string
data = open("users.txt" , "w" )
username = input("Sisesta siia oma kasutajanimi: ")

while True:
    password1 = input("Sisesta enda parool: ")
    password2 = input("Sisesta enda parool teist korda: ")
    if not password1 == password2:
            print("Viga paroolisisestamisel!")
            continue
    elif not len(password1) >= 8:
            print("Viga paroolisisestamisel!")
            continue
    elif password1.isalpha():
            print("Viga paroolisisestamisel!")
            continue
    elif password1.isdigit():
            print("Viga paroolisisestamisel!")
            continue
    elif str(password1).isalnum() == True:
        main_password = password1[::-1]
        data.write(username + ":" + main_password)
        break

data.close()   
