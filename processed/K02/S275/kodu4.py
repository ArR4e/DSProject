inglise = input("Lähtefaili nimi: ")
eesti = input("Sihtfaili nimi: ")

with open(inglise, 'r') as file :
    filedata = file. read()
    filedata = filedata.replace("Hello", "Tere")
 
with open(eesti, 'w') as file:
    file.write(filedata)

fail = open(inglise)

rida = fail.read().replace("\n", " ")
b = rida.count("Hello")
fail.close()

print("Tehti " + str(b) + " asendamist.")