def log():
    name = input("Siseta nimi: ")
    password_1 = input("Sisesta parool: ")
    password_2 = input("Sisesta parool teist korda: ")
    if password_1 == password_2:
        if len(password_1)<8:
            if str.isalnum(password_1) is True:
                new_password = input("Sisesta uus parool: ")
                with open("users.txt", "w") as file:
                    file.write("Kasutajanimi: " + name + '\n' + "Kasutaja parool: " + new_password)
                    file.close()
            else:
                print("Vale parool")
                log()
        else:
            print("Vale parool")
            log()           
    else:
        print("Vale parool")
        log()
log()
        