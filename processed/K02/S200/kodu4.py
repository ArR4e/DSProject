lähtefail = input("Lähtefaili nimi: ")
sihtfail = input ("Sihtfaili nimi: ")

lf = open(lähtefail, encoding='UTF-8')
sf = open(sihtfail, "w") 
hello_kokku = 0

for rida in lf:
    hello_kokku += rida.count('Hello')
    uus_rida = rida.replace('Hello','Tere')
    sf.write(uus_rida)

sf.close()
lf.close()

print(hello_kokku)
    

