f=open("taksohinnad.txt","r")
s=float(input("Sisesta tee pikkus kilomeetrites:"))
b=["x",9999,9999]
for line in f:
    a=line.split(",")
    if float(a[1])+float(a[2])*s < float(b[1])+float(b[2])*s:
        b=a
print("Kõige odavam on",b[0])