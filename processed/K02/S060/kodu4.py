sisse = input("Mis faili tõlkida:")
valja= input("Kuhu tõlkida seda:")
with open (sisse,"r") as f:
    l = f.readlines()
n = open(valja,"a")
ase=0
for rida in l:
    rida = str(rida)
    number = rida.count("Hello")
    if number > -0.5:
        
        ase=ase+number
    rida = rida.replace("Hello","Tere")
    #v.append(rida)
    n.write(rida)
print(ase)
n.close()
