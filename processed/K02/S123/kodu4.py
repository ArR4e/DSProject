lähte=input("Lähtefail: ")
siht=input("Sihtfail: ")

f=open(lähte, "r")
lf=f.read()

g=open(siht, "w")
sf=g.write(lf.replace("Hello","Tere"))
print(lf.count("Hello"))

f.close()
g.close()