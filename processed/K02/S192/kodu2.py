liini_pikkus = int(input("Sisesta liini pikkus meetrites: "))
max_postide_kaugus = int(input("Sisesta kõrvutiasetsevate postide maksimaalkaugus meetrites: "))
vastus = int(liini_pikkus / max_postide_kaugus) # Annab integral ehk täisarvulise vastuse
jäägiga_vastus = (liini_pikkus / max_postide_kaugus) # Annab float ehk ujukomaarvulise vastuse
if vastus == jäägiga_vastus and vastus != 1 and vastus != 2: # Kontrollib, kas vastus on täisarv ning ei oleks 1 ega 2.
    print(int(vastus))
elif vastus != jäägiga_vastus and jäägiga_vastus != 1 and jäägiga_vastus != 2: # Kontrollib, kas vastusel on tekkinud jääk, poleks 1 ega 2, ning liidab 2 (esimene post ka) juurde, et saaks tervet liini ära kasutada.
    print(int(vastus)+2)
elif jäägiga_vastus == 1 or jäägiga_vastus == 2: # On selleks, et anda tulemuseks 2, kui vastus peaks olema 1 või 2.
    print(int(vastus)+1)