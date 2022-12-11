fail = input("Sisesta faili nimi: ")
f = open(fail, encoding="utf-8")


for rida in f:
    jär = rida.strip().split(" ")
    
