liini_pikkus = int(input("Elektriliini pikkus: "))
posti_vahe = int(input("Postide vahe: "))
poste = (liini_pikkus/posti_vahe).__ceil__()#tester ütleb et __ceil__() ei tööta floati puhul
print(poste + 1)