# Aitas tähte ja numbrit kontrollida https://www.geeksforgeeks.org/python-program-to-check-if-a-string-has-at-least-one-letter-and-one-number/
# Reverse string https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python

while True:
    
    kasutajanimi = input("Sisesta kasutajanimi: ")
    esimene_parool = input("Sisesta parool esimest korda: ")
    teine_parool = input("Sisesta parool teist korda: ")

    if esimene_parool != teine_parool:
        # vale parool.
        print("Paroolid pole samad.\n")
        continue
    
    count = len(esimene_parool)
    
    if count < 8:
        # liiga lühike.
        print("Parool liiga lühike.\n")
        continue
    
    onTäht = False
    onNumber = False
    
    for char in esimene_parool:
        # läbib iga elemendi ja kontrollib.
        if char.isalpha():
            onTäht = True
        if char.isdigit():
            onNumber = True
            
    
    if onTäht == False or onNumber == False:
        # pole 1 tähte või numbrit.
        print("Pole ühte tähte või numbrit.\n")
        continue
    break

# Parool reverse.
reverse = "".join(reversed(esimene_parool))
# kuju muutmine
formatted = kasutajanimi + ":" + reverse

# Faili kirjutamine.
with open("users.txt", "w") as file:
    file.write(formatted)
    print("Success.")






