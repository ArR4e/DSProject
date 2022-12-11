k_nimi=input("Sisesta kasutajanimi: ")
try:
    while True:
        paro=input("Sisesta parool: ")
        paro2=input("Sisesta taas parool: ")
        if paro == paro2 and paro.isalnum == True and len(paro) >= 8:
            break
        else:
            if paro != paro2:
                print("Paroolid ei ole samad.")
                if len(paro) < 8:
                    print("Parool pole vähemalt 8.")
                    if paro.isalnum() != True:
                        print("Ei sisalda.")
            else:
                break
                
##        if paro != paro2:
##            break
##            print("Paroolid ei ole samad.")
##        if len(paro) < 8:
##            break
##            print("Parool peab olema vähemalt 8 tähemärki.")
##        if paro.isalnum() != True:
##            break
##            print("Parool ei sisalda nii tähti kui numbreid.")
except:
    raise ValueError()
taga=paro[::-1]
print(taga)
f=open("users.txt", "w")
f.write(str(k_nimi)+ ":"+str(taga))
f.close()