user = input("Sisesta nimi: ")

while True:
    pass1 = input("Sisesta salasõna: ")
    pass2 = input("Sisesta salasõna uuesti: ")

    if not pass1 == pass2:
        print("Paroolid ei ühti.")
        continue

    if len(pass1) < 8:
        print("Peab olema vähemalt 8 tähemärki.")
        continue

    if not any(i.isdigit() for i in pass1) and not any(i.isalpha() for i in pass1):
        print("Vähemalt 1 täht või 1 number.")
        continue

    with open("users.txt", "w", encoding="UTF-8") as i:
        i.write(f"{user}:{pass1[::-1]}")

    break
