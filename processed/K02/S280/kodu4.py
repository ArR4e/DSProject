# RP / 4. Masintõlge

eng = input("Lähtefaili nimi: ")
est = input("Sihtfaili nimi: ")

fail = open(eng, "r")
a = 0
b = []

for rida in fail:
    a += rida.count("Hello")
    rida = rida.replace("Hello", "Tere")
    b.append(rida.strip())
fail.close()

c = 0
fail = open(est, "w")
for rida in b:
    fail.write(b[b.index(rida)] + "\n")
fail.close()

print("Asendusi tehti: " + str(a))