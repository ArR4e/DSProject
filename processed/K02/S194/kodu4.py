a = input("Esimese faili nimi (koos failitüübi järelliitega): ")
b = input("Teise faili, kuhu tõlge kirjutatakse, nimi (koos failitüübi järelliitega): ")

with open(a, "r") as f:
    sisu = f.read()
    asenduste_arv = sisu.count("Hello")
    asendus = sisu.replace("Hello", "Tere")
    print(asendus)
    print("Tehti " + str(asenduste_arv)+ " asendust.")

with open(b, "w") as f2:
    f2.write(asendus)
