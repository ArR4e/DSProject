f1=input("inglisek faili nimi ")
f2=input("eestik faili sisu ")

fail1=open(f1)
fail2=open(f2,"w")
x=0
for rida in f1:
    f2.write(rida.replace("Hello","Tere"))
    x+=rida.count("Hello")

f1.close()
f2.close()
print(x)