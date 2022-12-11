nimi = input("Ütle oma kasutajanimi: ")

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
while a < 1 :
    kasutaja1= input("Kirjuta oma parool: ")
    kasutaja2= input("Korda oma parooli: ")
    if kasutaja1 == kasutaja2:
        b=1
    else:
        b=0
    if len(kasutaja1) >=8 :
        c = 1
    else:
        c = 0
    for sumbol in kasutaja1:
        try:
            sumbol = int(sumbol)
            if type(sumbol) is int:
                d = d + 1
            if type(sumbol) is str:
                e = e + 1
        except:
            if type(sumbol) is str:
                e = e + 1
    if d > 0 and e > 0:
        f = 1
    else:
        f=0
    if b + c + f == 3:
        a = 1
        
tagurpidi =''.join(reversed(kasutaja1)) #https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
               # kasutasin abi sellelt lehekuljelt, leidsin kasu reversed, aga saidilt saadud kask join, mille ees on tuhi string, mida hakatakse taitma tuli sealt. 
kirjutamine = open('users.txt',"w")
oige = nimi + ":" + tagurpidi
print(oige)
kirjutamine.write(oige)
kirjutamine.close()