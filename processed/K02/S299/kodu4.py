f = open('inglise.txt')

rida1 = f.readline().replace('Hello','Tere')

rida2 = f.readline().replace('Hello','Tere')

rida3 = f.readline().replace('Hello','Tere')

f.close()

f2 = open('eesti.txt','w')

f2.write(rida1 + '\n')

f2.write(rida2 + '\n')

f2.write(rida3 + '\n')

f2.close()

uus_tekst = rida1 + rida2 + rida3

asenduste_arv =(uus_tekst).count('Tere')

print(asenduste_arv)