f1 = open("koerad.txt", "w", encoding="UTF-8")
f1.write("Hispaania koeratõud‎" + "\n")
f1.write("Portugali koeratõud‎" + "\n")
f1.write("Tai koeratõud" + "\n")
f1.write("Tiibeti koeratõud‎" + "\n")

f1 = open("koerad.txt")
faili_sisu = f1.read()
print(faili_sisu)
print("Tehti", 'koeratõud'.count('koeratõud'), "asendamist")
f2 = open("snuutid.txt", "w")
for x in f1.readlines():
    f2.write(x)
f1.close()
f2.close()

f2 = open("snuutid.txt", "w")
"koeratõud".replace("koeratõud","snuutid")
faili_sisu = f2.read()
print(faili_sisu)
f2.close()

# Ma ei oska :(   
