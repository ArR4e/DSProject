lahtefail=input('Sisestage lahtefail: ')
sihtfail=input('Sisestage sihtfail: ')

f1=open(lahtefail)
tekst=f1.read()
f1.close()

f2=open(sihtfail, 'w')
f2.write(tekst.replace('Hello', 'Tere'))
f2.close()

print('Tehti '+str(tekst.count('Hello'))+' asendamist.')