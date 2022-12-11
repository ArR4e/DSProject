from string import *
nimi= str(input("Sisesta kasutajanimi:"))
while True:
    try:
        par1= str(input("Sisesta parool:"))
        par2= str(input("Sisesta parool uuesti:"))
        if par1 != par2:
            print("paroolid on erinevad")
            int(üks)
            #eelnev rida on excepti liikumiseks
        if len(par1)<8:
            print("parool on liiga lühike")
            int(üks)
        if par1.isalpha() == True or par1.isdigit() == True:
            print("parool peab sisaldama nii tähti kui tähemärke")
            int(üks)
        
    except:
        continue
    break
par3=par1[len(par1)::-1]

f=open("users.txt","w")
f.write(nimi+":"+par3)
f.close()