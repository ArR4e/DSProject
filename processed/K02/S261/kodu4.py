x=str(input('Sisesta lähtefaili nimi: '))

y=str(input('Sisesta sihtfaili nimi: '))

f=open(x)

sisu=f.read()

f.close()

sisu.replace('Hello','Tere')
print('Tehti',sisu.count('Hello'),'asendamist.')

f=open(y,'w')
f.write(sisu.replace('Hello','Tere'))
f.close()

