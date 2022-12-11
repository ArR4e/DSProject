kasutajanimi = input("Sisestage kasutajanimi: ")
while True:
    parool1 = input("Sisestage parool: ")
    parool2 = input("Sisestage uuesti parool: ")
    
    if parool1 != parool2:
        print("Esimene parool kattub teise parooliga!")
        
    else:
        parool = parool1
        if len(parool) < 8:
            print("Parool pole piisavalt pikk!")
        
        else:
            if parool.isnumeric():
                print("Parool peab sisaldama tähti!")
                
            else:
                if any (char.isdigit() for char in parool):
                    break
        
def tagurpidi(parool):
    tagurp = "". join(reversed(parool))
    return tagurp
loorap = tagurpidi(parool)

fail = open("users.txt", "w")
sisu = ":". join((str(kasutajanimi), str(loorap)))
fail.write(sisu)
fail.close()