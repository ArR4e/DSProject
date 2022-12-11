f1 = input("Sisestage esimese faili nime: ")
f2 = input("Sisestage teise faili nime: ")

#Loeme teksti esimesest failist
f1 = open(f1)
f1_sisu = f1.read()
#Vahetame sõnad ja arvutame vahetusi
text = f1_sisu.replace('Hello', 'Tere')
n = f1_sisu.count('Hello')
f1.close()

#Paneme teksti teise faili sisse
f2 = open(f2, 'w')
f2.write(text)
n = str(n)
print('Tehti', n, 'asendamist')
f2.close()