nimi = input("Sisesta oma nimi:")
while True:
    parool = input("Sisesta parooli:")
    parool2 = input("Sisesta parooli teist korda:")
    if parool != parool2:
        print("Proovi uuesti.")
        continue
    elif len(parool) < 8:
        print("Parool peab olema vähemalt 8 märki pikk.")
        continue
    elif parool.isalpha() or parool.isnumeric():
        print("Parool peab koosnema tähtedest ja numbritest.")
        continue
    else:
        break

def is_palindrome(password):
    reversed_parool = password[::-1]
    return reversed_parool

tekst = nimi + ":" + is_palindrome(parool)

f = open("users.txt", "w")
f.write(tekst + "\n")
f.close()