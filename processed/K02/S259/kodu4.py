esimene = input("Sisesta esimese faili nimi: ")
teine = input("Sisesta teise faili nimi: ")

file1open = open(esimene, "r")
file2open = open(teine, "w")
file1tekst = file1open.readlines()
asendusi = 0

for line in file1tekst:
    if "Hello" in line:
        mitu = line.count("Hello")
        file2open.write(line.replace("Hello", "Tere"))
        asendusi += mitu
    else:
        file2open.write(line)
        
print("Asendusi tehti: " + str(asendusi))

file1open.close()
file2open.close()