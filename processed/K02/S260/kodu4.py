fail1 = input("Sisestage faili nimi: ")
fail2 = input("Sisestage faili nimi: ")

f = open(fail1,encoding="utf-8")
nf = open(fail2,"a")
d = f.readlines()
asendusi = 0
for line in d:
    asendusi += line.count("Hello")
    line = line.replace("Hello","Tere")
    nf.write(line)
    
print("Tehti "+str(asendusi)+" asendust.")
f.close()
nf.close()