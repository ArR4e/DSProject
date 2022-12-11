Lähtefail = input("Sisesta lähtefaili nimi: ")
Sihtfail = input("Sisesta sihtfaili nimi: ")
with open(Lähtefail, "r") as rf:
    with open(Sihtfail, "w") as wf:
        for line in rf:
            wf.write(line.replace("Hello", "Tere").replace("HELLO", "TERE").replace("hello", "tere"))
            
file = open(Lähtefail)
data = file.read()
esinemissagedus1 = (data.count("Hello"))
esinemissagedus2 = (data.count("HELLO"))
esinemissagedus3 = (data.count("hello"))
esinemissagedus4 = (data.count("Hello-Hello"))
print("Tehti " + str(esinemissagedus1 + esinemissagedus2 + esinemissagedus3 + esinemissagedus4) + " asendust")
file.close()