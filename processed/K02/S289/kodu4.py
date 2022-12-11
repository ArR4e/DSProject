lähtefail = input("Palun sisesta lähtefaili nimi: ")
sihtfail = input("Palun sisesta sihtfaili nimi: ")

f1 = open('lähtefail.txt', encoding='UTF-8')
f2 = open('sihtfail.txt', encoding='UTF-8')

for rida in f1:
    x = f1.count("hello")
    f2.write(rida.replace("hello", "Tere"))
f1.close()
f2.close()
print(x)


