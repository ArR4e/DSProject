olemasfail = str(input("Sisesta lähtefailinimi: "))
uus = str(input("Sisesta sihtfaili nimi: "))


f = open(olemasfail, "r")


a = open(uus, "w")
summa = 0

for i in f:
    summa += i.count("Hello")
    i = i.replace("Hello", "Tere")
    a.write(i)
    

print("Tehti " + str(summa) + " asendamist.")

a.close()