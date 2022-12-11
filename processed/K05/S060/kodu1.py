kasutajanimi=str(input("Milline on teie soovitud kasutajanimi: "))
a=open("users.txt","w")
b=0
n=0
while True:
    parool1=str(input("Parool: "))
    parool2=str(input("Parool uuesti: "))
    while True:
        if parool1 !=parool2:
            print("Parool ei ole sama")
            break
        elif len(parool1) <8:
            print("Pikkus on liiga lühike")
            break
        elif not any(char.isdigit() for char in parool1):
            print("Mõni võiks number olla")
            break
        elif not any(char.islower() for char in parool1):
            print("Mõni mõiks täht olla")
            break
        else:
            p=parool1[::-1]
            b=1
            break
    
    
    if b==1:
        break
    n+=1
    if n==2:
        break
    
if n <1:
    a.write(kasutajanimi+":"+p)
a.close()
        