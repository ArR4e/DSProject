username = ""
password = ""

TEXT_USERNAME = "Sisesta siia oma kasutajanimi: "
TEXT_PASSWORD_1 = "Sisesta siia oma parool: "
TEXT_PASSWORD_2 = "Sisesta siia parool uuesti: "

def isGreaterThan(s, length):
    return len(s) >= length
        
def containsNumber(s):
    return any(i.isdigit() for i in s)

def containsLetter(s):
    return any(i.isalpha() for i in s)
        
def reverseString(s):
    return s[::-1]
    
def writeToFile():
    f = open("users.txt", "a")
    f.write(username + ":" + password + "\n")
    f.close()

while True:
    input_username = input(TEXT_USERNAME)
    input_password1 = input(TEXT_PASSWORD_1)
    input_password2 = input(TEXT_PASSWORD_2)

    if input_password1 != input_password2:
        print("Parool pole sama")
        continue
    
    if not isGreaterThan(input_password1, 8):
        print("Parool on lühem kui " + str(8) + " tähemärki")
        continue
        
    if not containsNumber(input_password1):
        print("Pole numbrit")
        continue
        
    if not containsLetter(input_password1):
        print("Pole tähte")
        continue
    
    username = input_username
    password = reverseString(input_password1)
    break
    
writeToFile()




