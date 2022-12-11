from pykkar import *

# Olgu antud maailm ja pykkar
# Alguses las pykkar leiab seina
while not is_wall():
    step()

#Siis pööratame teda ja paneme liikuma kuni ta jõuab nurgasse
#Ta kindlasti liigub mööda seina, mistõttu kui tal ees on uus sein, siis ta on nurgas
#Kui ta on nurka jõudnud, ta värvib seda
#Algoritm kordub kuni pykkar jõuab juba värvitud nurgasse
while True:
    right()
    while not is_wall():
        step()
    if is_painted():
        break
    else:
        paint()
    
