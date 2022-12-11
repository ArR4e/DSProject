with open(input("Lähtefaili nimi: "), "r") as f:
    with open(input("Sihtfaili nimi: "), "w") as g:
        a = f.readlines()
        print("Tehti " + str(sum([l.count("Hello") for l in a])) + " asendamist.")
        [g.write(l.replace("Hello", "Tere")) for l in a]