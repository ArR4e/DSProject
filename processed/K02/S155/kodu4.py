#küsib kasutajalt
leht = input("sisestage fail tõlkimiseks:  ")
leht2 = input("sisestage fail kuhu tõlkida:  ")
#avab esimese
f = open(leht)
inglise = f.read()
    #b = f.readline()
    #c = f.readline()
f.close()
#print(inglise)
#tõlgib tervitused
eesti = inglise.replace('Hello', 'Tere')
teisendus = inglise.count('Hello')
#avab teise
f = open(leht2, "w")
f.write(eesti + "\n")
    #f.write(b + "\n")
    #f.write(c + "\n")
f.close()
print(teisendus)