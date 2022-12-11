file_to_read = input("Sisesta fail, mida lugeda: ")
write_to_file = input("Sisesta fail, kuhu kirjutada: ")

sisu = open(file_to_read, "r") #lahenduse idee leidsin stackoverflowst, muutsin konteksti ja püüdsin ebavajalikku eemaldada
data = sisu.read()
sisu.close()

uusfail = open(write_to_file, "a+")
uusfail.write(data)
arv = data.count("Hello")
uusfail.close()

import re #proovisin eelnevalt veel mitut netist soovitatud lahendust, kuid ei töötanud ükski. Lõpuks otsustasin Regexiga proovida ja õnnestus.

with open(write_to_file, 'r+') as f: 
    text = f.read()
    text = re.sub('Hello', 'Tere', text)
    f.seek(0)
    f.write(text)
    f.truncate()
    
print("Tehti " + str(arv) + " asendamist.")