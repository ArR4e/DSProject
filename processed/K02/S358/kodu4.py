total = 0
lfile=open(input("Lähtefaili nimi: "), "r")
sfile=open(input("Sihtfaili nimi: "), "w")

for row in lfile:
    total += row.count("Hello")
    rand=row.replace("Hello", "Tere")
    print(rand)
    sfile.write(rand)
    
print("Tehti " + str(total) + " asendamist.")
sfile.close()