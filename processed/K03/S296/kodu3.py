n = int(input("Sisesta naturaalarv:"))
ruudud=0
x=0
while ruudud<=n:
    x=x+ruudud**2
    ruudud+=1
sumruut=0
y=0
while sumruut<=n:
    y=y+sumruut
    sumruut+=1
print(y**2-x)
    