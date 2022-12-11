lähtefail = input("Lähtefaili nimi: ")
sihtfail = input("Sihtefaili nimi: ")

fail = open(lähtefail, encoding="UTF-8")
data = fail.read()
x = data.replace("Hello", "Tere")
count = data.count("Hello")
print("Tehti", count, "asendamist.")

f = open(sihtfail, "w")
f.write(x)
f.close()
    
