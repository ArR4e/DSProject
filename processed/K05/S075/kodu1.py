nimi=input("Sisesta kasutaja nimi: ")
parool1=input("Sisesta parool esimest korda: ")
parool2=input("Sisesta parool teist korda: ")

while True:
    if parool1==parool2:
        a=len(parool1)
        if a>=8:
            b=bool(parool1.isnumeric())
            if b == False and bool(parool1.isalpha())==False:
                c=0
                d=""
                while a>c:
                    d=d+parool1[a-1]
                    a-=1
                print(d)    
                break
            else:
                print("Parool ei sisaldanud numbreid ja tähti.")
        else:
            print("Parool peab olema vähemalt 8 tähemärki.")
    else:
         print("Esimene ja teine parool ei ole samasugused.")
    parool1=input("Sisesta parool esimest korda: ")
    parool2=input("Sisesta parool teist korda: ")

f=open("users.txt","w")
f.write(nimi+":"+d)
f.close()