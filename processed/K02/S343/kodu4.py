a=input('lähtefail: ')
b=input('sisendfail: ')

lahtefail = open(a)
sisendfail = open(b, 'w+')
sisu=lahtefail.read()

sisendfail.write(sisu.replace("Hello", "Tere"))


tõlgetearv = sisu.count("Hello")
print("Tõlkeid tehti " + str(tõlgetearv) + "tükki.")

lahtefail.close()
sisendfail.close()
