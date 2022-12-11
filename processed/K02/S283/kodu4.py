l_fail = input("Lähtefaili nimi: ")
s_fail = input("Sihtfaili nimi: ")

lähte = open(l_fail)
lähte_sisu = lähte.read()
asendused = lähte_sisu.count("Hello")
a = (lähte_sisu.replace("Hello", "Tere"))
print("Tehti ", (asendused)," asendamist." )
s = open(s_fail, "w")
s.write(a)

s.close()
lähte.close()
#closeda saab alles peale seda, kui on info üle kantud või omistatud millelegi

