fail1=str(input("Lähtefaili nimi:"))
fail2=str(input("Sihtfaili nimi:"))

f=open(fail1)
faili_sisu=f.read()

n=str(faili_sisu.count('Hello'))
print('Tehti '+ n +' asendamist.')

f=open(fail2,'w')
f.write(faili_sisu.replace('Hello','Tere'))

f.close()
#print(faili_sisu.replace('Hello','Tere'))





