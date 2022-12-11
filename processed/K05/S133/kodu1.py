nimi=str(input("Teie nimi palun: "))
a=0
numbrid=0
tähed=0
parool3=""
e=0
while a==0:
    c=0
    parool=str(input("Teie parool, palun: "))
    parool2=str(input("Teie parool uuesti, palun: "))
    if parool != parool2:
        break
    if len(parool)<8:
        break
    for character in parool:
        if character.isalpha() :
            tähed=1
        if character.isdigit() :
            numbrid += 1
    if numbrid == 0 or tähed ==0:
        break
    e=len(parool)
    e-=1
    a=1
while a==1:
    if e < 0:
        a=0
        break
    
    parool3+=parool[e]
    e-=1
b = open("users.txt","w")
b.write(nimi)
b.write(":")
b.write(parool3)
b.close()
