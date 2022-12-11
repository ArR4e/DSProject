kasutajanimi = input("Sisestage kasutajanimi: ")
error1 = 0
error2 = 0
error3 = 0
while True:
    if error1 == 1:
        print("Sisestatud paroolid erinevad!")
    elif error2 == 1:
        print("Parool peab sisaldama vähemalt 8 tähemärki!")
    elif error3 == 1:
        print("Parool peab sisaldama nii tähti kui numbreid!")
    parool = input("Sisestage parool: ")
    pparool = input("Sisestage uuesti parool: ")
    if parool == pparool:
        error1 = 0
        if len(parool) >= 8:
            error2 = 0
            if (parool.isalpha() == False) and (parool.isnumeric() == False):
                error3 = 0
                break
# isalpha ja isnumeric commandid saadud allolevast lingist
# https://stackoverflow.com/questions/64862663/how-to-check-if-a-string-is-strictly-contains-both-letters-and-numbers
            else:
                error3 = 1
        else:
            error2 = 1
    else:
        error1 = 1
                
# reverse meetod: https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python                
enc = parool[len(parool):: -1] #vaese mehe encryption

f = open("users.txt", "w") #praktilises kasutuses peaks täidetud rea skippima
f.write(kasutajanimi + ":" + enc) #praegu overwriteib samale reale uusima
f.close()                  #kui programmi mitu korda runnida