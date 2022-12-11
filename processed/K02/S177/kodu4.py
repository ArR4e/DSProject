a = input ("Sisestage lähtefaili nimi:") + (".txt")
b = input ("Sisestage sihtfaili nimi: ") + (".txt")
with open (a) as f:
    lines = f.read ()
    asendused = (lines.count("Hello"))
with open (b, "w") as l:
    l.write(lines.replace("Hello", "Tere"))
print ("Tehti", asendused, "sõna asendamist.")
f.close()
l.close()