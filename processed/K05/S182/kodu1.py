kasutajanimi=input("Sisestage kasutajanimi: ")
parool1=input("Sisestage parool: ")
parool2=input("Sisestage parool uuesti: ")
while True:
    if parool1==parool2:
    
        if len(parool1)>= 8:

            if bool(parool1.isnumeric()) ==False and bool(parool1.isalpha())==False:
                a=(parool1[::-1])
                break
            else:
                print("Paroolis peavad olema nii tähed kui numbrid")
        else:
            print("Paroolis peab olema vähemalt 8 tähemärki")
    else:
        print("Esimene parool ei kattu teisega")
    parool1=input("Sisestage uus parool: ")
    parool2=input("Sisestage uus parool uuesti: ")
g=open("users.txt","w")
g.write(kasutajanimi+":"+a)
g.close()