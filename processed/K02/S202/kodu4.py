lf = input("Sisesta lähtefaili nimi: ") #lf = l(ähte)f(ail)
sf = input("Sisesta sihtfaili nimi: ") #sf = s(iht)f(ail)
f1 = open(str(lf))
f2 = open(str(sf), "w")

fs= f1.read() #fs = f(aili)s(isu)
mh = fs.count("Hello")  #loeb mitu Hello'd on algses failis
f1.close()


f2.write(fs.replace("Hello", "Tere"))
f2.close()

print("Tehti " + str(mh) + " asendamist")


