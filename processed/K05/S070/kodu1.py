def containsNumber(value): #Võtsin selle funtsiooni netist, tutvusin sellega kuidas see töötab
    for character in value:
        if character.isdigit():
            return True
    return False

nimi = input("Sisestage kasutajanimi ")
STATE = "PAROOL"
while True:
    if STATE == "PAROOL":
        pas1 = input("Sisestage parool ")
        STATE = "PAROOL2"
    if STATE == "PAROOL2":
        pas2 = input("Sisestage parool uuesti ")
        if pas1 == pas2 and len(pas1)>=8 and containsNumber(pas1) and any(c.isalpha() for c in pas2):
            break
        else:
            print("Midagi on valesti")
            STATE = "PAROOL"
pas1 = pas1[::-1]
fail = open("users.txt", "w")
fail.write(nimi+":"+pas1)
fail.close()
            