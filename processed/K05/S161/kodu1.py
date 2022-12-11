nimi= input("Sisestage oma nimi: ")
parool1=input("Sisestage parool: ")
parool2=input("Sisestage parool: ")
parool3=parool1.lower()
parool4=0
numbrid= False
fail=open("users.txt", "w")
if parool1!=parool2:
    print("Paroolid ei ühti omavahel")
else:
    if len(parool1)<8:
        print("Parool peab olema vähemalt 8 tähemärki!")
    else:
        if parool3.islower():
            for rida in parool3:
                if rida.isdigit():
                    parool4=parool1 [::-1]
                    numbrid=True
            if numbrid!=True:
                print("Parool peab sisaldama numbreid!")
        else:
            print("Parool peab sisaldama tähti!")
if numbrid==True:
    fail.write(nimi +":" + parool4)
    fail.close()
    