f=input("Sisesta esimese faili nimi:")
h=input("Sisesta uue faili nimi:")

a=open(f)
faili_sisu=a.read()
print(faili_sisu.count("Hello"))
faili_sisu=faili_sisu.replace("Hello","Tere")
a.close()
    
s=open(h,"w")
s.write(faili_sisu)
s.close()


