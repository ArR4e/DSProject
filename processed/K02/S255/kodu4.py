import re
with open(input("sisesta inglisekeelse tekstifaili nimi: "), "r") as ava_eng:
    Tere_Est, count = re.subn("Hello", repl = "Tere", string = ava_eng.read())
with open(input("sisesta eestikeelse tekstifaili nimi: "), "w+") as ava_est:
    ava_est.write(Tere_Est)
    print(f"Tehti {count} asendamist.")