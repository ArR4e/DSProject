sissefail = open(str(input("Sisesta lähtefaili nimi:")),"r")
väljafail = open(str(input("Sisesta sihtfaili nimi:")),"w")
text = sissefail.read()
asendused = text.count("Hello")
asendused += text.count("hello")
print("Tehti " + str(asendused) + " asendamist.")
tekxt = text.replace("Hello","Tere")
tekst = tekxt.replace("hello","tere")
väljafail.write(tekst)
väljafail.close()

