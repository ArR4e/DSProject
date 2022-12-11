f = input("Sisesta failinimi: ")
fail = open("f", encoding="UTF-8")
for rida in fail:
    puhas = rida.strip().split(" ")
    print(puhas)