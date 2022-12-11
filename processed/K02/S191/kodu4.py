F=str(input("Tõlgitav fail: "))
G=str(input("Tõlgitud fail: "))

f=open(F)

sisu=f.read()
f.close()

arv1=sisu.count("Hello")
arv2=sisu.count("hello")+arv1

tõlge1=sisu.replace("Hello","Tere")
tõlge2=tõlge1.replace("hello","tere")

g=open(G, "w")
g.write(tõlge2+"\n")
g.close()

print("Tehti",arv2,"muudatust")