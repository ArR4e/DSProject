teepikkus = float(input("Sisesta tee pikkus kilomeetrites: "))
f = open("taksohinnad.txt","r")
summa = 99999999
taksonimi = ''
while True:
    x = f.readline().strip('\n')
    if x ==(''):
        break
    y = x.split(",")
    vahesumma = float(y[1])+ teepikkus*float(y[2])
    if vahesumma < summa:
        summa = vahesumma
        taksonimi = y[0]
    
print("Odavam on",taksonimi)
f.close()