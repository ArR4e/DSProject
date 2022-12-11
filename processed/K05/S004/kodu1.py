username=str(input("Kasutajanimi: "))
loendur1=0
loendur=0
f=open("users.txt","w")
while True:
    parool=str(input("Parool: "))
    parool2=str(input("Korda parooli: "))
    if parool2 != parool:
        continue
    if len(parool)<8:
        continue
    for x in parool:
        if x.isdigit()==True:
            loendur1+=1
        elif x.isdigit()==False:
            loendur+=1
    if loendur1<1 or loendur<1:
        continue
    parool = parool[::-1]
    f.write(username+":"+parool)
    f.close()
    break