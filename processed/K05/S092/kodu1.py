def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def reverse(x):
  return x[::-1]

usr = input("Sisetage kasutajanimi: ")

while True:
    passwd = input("Sisestage parool: ")
    passwd2 = input("Sisestage parool teist korda: ")

    if passwd == passwd2 and len(passwd) >= 8 and passwd.upper().isupper() and has_numbers(passwd):
        passwd_reversed = reverse(passwd)
        
        file = open("users.txt", "w", encoding="UTF-8")
        file.write(usr + ":" + passwd_reversed)
        file.close()
        break
    else:
        print("Parool peab kattuma esimese, sisaldama vähemalt kaheksat tähemärki ning peab sisaldama nii tähti kui numbreid")