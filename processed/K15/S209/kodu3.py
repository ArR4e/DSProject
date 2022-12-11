f = input("Sisesta failinimi: ")
fail = open(f)

aa = []

for rida in fail:
    rida = rida.strip().split(" ")
    aa.append(rida)
    
print(aa)