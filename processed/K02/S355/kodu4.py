algFail = input("Sisesta avatava faili nimi: ")
lõppFail = input("Sisesta tehtava faili nimi: ")

with open(algFail, "rt") as fin:
 with open (lõppFail, "wt") as fout:
  for line in fin:
   fout.write(line.replace("Hello", "Tere"))

txt = open(algFail, "r")
loe = txt.read()
helloArv = loe.count("Hello")
print ("Tehti " + str(helloArv) + " asendamist")
