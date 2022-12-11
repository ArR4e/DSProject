f_in = open(input("Ava fail: "))
f_out = open(input("Kirjuta faili: "), "w")

faili_sisu = f_in.read()
asendus = faili_sisu.count("Hello")
f_out.write(faili_sisu.replace("Hello","Tere"))
print("Asendati " + str(asendus)+" sõna.")

f_in.close()
f_out.close()