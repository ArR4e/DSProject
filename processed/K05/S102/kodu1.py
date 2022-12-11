tunnus=input('Palun sisestage soovitud kajutajatunnus :')

def kontroll(parool1):
    for taht in parool1:
        if taht.isdigit():
            return True

while True:
    parool1=input('Palun sisestage soovitud parool :')
    parool2=input('Palun sisestage parool uuesti :')
    if parool1==parool2 and len(parool1)>7 and kontroll(parool1):
        break

f=open("users.txt", "w")
parool2=""
for taht in parool1:
    parool2=taht+parool2

f.write(tunnus+":"+parool2)
f.close()


