kasutajanimi=input("Sisesta kasutajanimi: ")
while True:
    parool1=input("Sisesta parool esimest korda: ")
    parool2=input("Sisesta parool uuesti: ")
    if parool1==parool2:
        if len(parool1)>=8:
            if parool1.isalpha() or parool1.isnumeric():
                print("Parool peab sisaldamanii tähti kui numbreid.")
            else:
                break      
        else:
            print("Parool peab olemavähemalt 8 tähemärki pikk.")        
    else:
        print("Paroolid ei ühti!")
parool=parool1[::-1]#https://stackoverflow.com/questions/931092/reverse-a-string-in-python
f=open('users.txt','w')
f.write(kasutajanimi+':'+parool)
f.close()