a = input("Sisestage esimese faili nimi: ")
b = input("Sisestage teise faili nimi: ")

esimeneF = open(a, 'r')
sisu_uks = esimeneF.read()
tered = sisu_uks.count("Hello")
muudatus = sisu_uks.replace("Hello", "Tere")
esimeneF.close()

teineF = open(b, 'w')
teineF.write(muudatus)
teineF.close()

print("Asendusi oli: ", tered)