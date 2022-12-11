km=float(input("Sisesta teekonna pikkus: "))
fail=open("taksohinnad.txt")

x1=fail.readline().strip().split(",")
h=[""]
if x1==h:
    print("Taksot pole!")
    fail.close()
    exit()
else:
    pass
hind1=float(x1[1])+(float(x1[2])*km)
x2=fail.readline().strip().split(",")
hind2=float(x2[1])+(float(x2[2])*km)
x3=fail.readline().strip().split(",")
hind3=float(x3[1])+(float(x3[2])*km)

if hind1<hind2 and hind1<hind3:
    print(x1[0])
elif hind2<hind3 and hind2<hind1:
    print(x2[0])
elif hind3<hind2 and hind3<hind1:
    print(x3[0])
    
fail.close()