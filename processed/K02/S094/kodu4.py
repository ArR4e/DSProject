import time # sleepi jaoks


inglise_fail = input("Sisesta faili nimi mida tõlkida: ")
eesti_fail = input("Sisesta faili nimi kuhu tõlge läheb: ")

try:
    f1 = open(inglise_fail, "r")
except:
    print("Viga tõlgitava faili avamisel, sulgumine..")
    time.sleep(5) # sleep 5 sekundit ja seejärel sulgub.
    exit()
    
# kui faili avamine õnnestus siis läheb siit edasi.
file = f1.read() # loeb faili sisu.
hello_count = file.count("Hello")
translate = file.replace("Hello","Tere")

try:  
    f2 = open(eesti_fail, "w")
except:
    print("Viga tõlketulemuste avamisel, sulgumine..")
    time.sleep(5) # sleep 5 sekundit ja seejärel sulgub.
    exit()
    
f2.write(translate)

print("Tehti " + str(hello_count) + " asendamist " + eesti_fail + " faili.")
f1.close()
f2.close()