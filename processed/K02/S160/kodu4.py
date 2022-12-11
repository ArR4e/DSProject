a= open(input("Sisesta lähtefaili nimi: "));b = open(input("Sisesta sihtfaili nimi: "), "w"); count = 0
for x in a:
    if "Hello" in x:count+=x.count("Hello");x = x.replace("Hello","Tere");b.write(x)
    else:b.write(x)
b.close();a.close();print("Tehti " + str(count) +" asendust.")