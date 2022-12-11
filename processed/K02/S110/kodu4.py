# esitatud hiljem

fail = input('Lähtefaili nimi: ')
fail_uus = input('Sihtfaili nimi: ')

f = open(fail, 'r')

sisu = f.read() #loeb esimest faili

a = open(fail_uus, 'w' ) #avab uue 

c = sisu.replace('Hello', 'Tere')
b = a.write(c)
asendused = c.count('Tere') #loeb tere-asendused üle

print('Tehti '+ str(asendused) +' asendamist.')