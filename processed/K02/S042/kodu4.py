import re

l2hte = input("Lähtefaili nimi: ")

try:
    with open(l2hte) as fail_1:
        read = fail_1.readlines()
        tulem = []
        arv = 0
        for rida in read:
            arv += rida.count("Hello")
            tulem.append(re.sub("Hello", "Tere", rida))

        siht = input("Sihtfaili nimi: ")
        fail_2 = open(siht, "w")
        fail_2.writelines(tulem)
        fail_1.close()
        fail_2.close()
        print("Tehti " + str(arv) + " asendamist.")

except FileNotFoundError:
    print("Sellise nimega faili pole!")
