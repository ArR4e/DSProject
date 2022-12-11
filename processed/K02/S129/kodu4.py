import fileinput

fail1 = input("Lähtefaili nimi: ")
fail2 = input("Sihtfaili nimi: ")

with open(fail1) as f:
    lines_raw = f.read()

eestitekst1 = lines_raw.replace("Hello", "Tere")

with open(fail2, "x") as e:
    e.write(eestitekst1)

lines = lines_raw.lower()
asendused = lines.count("hello")

print("Tehti " + str(asendused) + " asendamist")