a=input("Esimene fail: ")
b=input("Teine fail: ")
f=open(a, "r")
d=f.read()
d=d.lower()
d=d.replace("hello", "tere")
f.close()
f=open(b,"w")
f.write(d)
f.close()



