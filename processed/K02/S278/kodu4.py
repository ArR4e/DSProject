

A = input("Sisesta palun esimese faili nimi: ")
B = input("Sisesta palun teise faili nimi: ")

fail1 = open(A, "r")
fail2 = open(B, "w")
teine = 0
for i in fail1:
    teine += i.count("Hello")
    teised = i.replace("Hello", "Tere")
    fail2.write(teised)
    
print(str(teine) + " asendamist on tehtud")
    
fail1.close()
fail2.close()
