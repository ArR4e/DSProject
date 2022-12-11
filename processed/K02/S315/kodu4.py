a = input("Kust failist soovid tõlkida? ")
b = input("Kuhu faili soovid asendused viia? ")

f = open(a,"r+")
vana = f.read()
f.close()

uus = vana.replace("Hello", "Tere").replace("hello","tere")

vanas1 = vana.count("Tere")
vanas2 = vana.count("tere")

x = uus.count("Tere")
y = uus.count("tere")

f = open(b,"a")
f.write(uus)
f.close()

print(x+y-vanas1-vanas2)

