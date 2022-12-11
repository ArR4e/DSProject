tee=float(input("Sisesta tee pikkus koju kilomeetrites: "))

f=open("taksohinnad.txt", encoding="utf-8")

järjend=[]
for i in f:
    i=i.strip()
    i=i.split(",")
    järjend.append(i)

f.close()

try:
    hind=float(järjend[0][1])+float(järjend[0][2])*tee
    odavaim=järjend[0][0]
    i=1
    while i < len(järjend):
            if hind > float(järjend[i][1])+float(järjend[i][2])*tee:
                hind=float(järjend[i][1])+float(järjend[i][2])*tee
                odavaim=järjend[i][0]
                i+=1
            else:
                i+=1
            
    print("Kõige odavam on " + odavaim +".")
except:
    print("Fail taksohinnad.txt on tühi!")


    
