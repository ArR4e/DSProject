'''Kirjuta programm, mis realiseerib ühe veebilehe registreerimisvormi algoritmi.'''
'''******************************'''
def on_numbreid(sone):
    numbreid = 0
    for i in range(9): # numbrite 0..9 järgi
        if str(i) in sone: # kui number 'i' leidub sones
            numbreid += 1 # suurenda 'numbreid'
    if numbreid != 0:
        return True
    return False
'''******************************'''
def tagurpidi(sone):
    pooratud = ""
    for i in reversed(range(len(sone))):
        pooratud += sone[i]
    return pooratud
'''******************************'''
print("*"*100)
print("Tere tulemast meie veebilehe registreerimisvormi. Täida vorm.")
print("*"*100)

kasutajanimi = input("Kasutajanimi: ").strip()

# salasõnad on küsitud kuni pole sisestatud korralikult
while True:
    salasona_ = input("Salasõna: ").strip()
    salasona = input("Korda salasõna: ").strip()
        
    # kas teine salasõna kattub esimesega
    if salasona != salasona_:
        print("Salasõnad ei ole võrdsed. Sisesta uuesti.")
    # kas on salasõna pikkus vähemalt 8 tähemärki
    if len(salasona) < 8:
        print("Salasõna peab olema vähemalt 8 tähemärki pikk. Sisesta uuesti.")
    # ning koosneb mitte ainult numbritest või ainult tähtedest
    elif on_numbreid(salasona) == False or salasona.isdigit():
        print("Salasõna peab koosnema nii tähtedest kui ka numbritest.")
    # kui kõik ülespool tingimused olid täidetud, siis katkesta
    else:
        break

# avame faili "users.txt" loomiseks või ülekirjutamiseks
# salvestame faili ning paneme faili kinni
f = open("users.txt", "w")
f.write(kasutajanimi+":"+tagurpidi(salasona))
f.close()

print("*"*100)
print("Täname. Teie andmed on salvestatud.")
print("*"*100)