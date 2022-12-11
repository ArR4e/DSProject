kasutaja = input("Sisesta kasutajanimi: ")

while True:
    passw1 = input("Sisesta password: ")[::-1]
    passw2 = input("Sisesta password teist korda: ")[::-1]
    if passw1 != passw2:
        continue
    if len(passw1) < 8:
        continue
    if any(passw1.isdigit() for i in passw1) > 0:
        continue
    else:
        break
with open("users.txt", "a") as f:
    f.writelines(kasutaja + ":" + passw1)
f.close()


