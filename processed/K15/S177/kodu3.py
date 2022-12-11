bussid = []
valik = []
dokument = input ("Sisesta faili nimi: ")

fail = open(dokument, encoding="UTF-8")
for rida in fail:
    rida = rida.strip("\n")
    x = rida.split(" ")

#    print (x)
    bussid.append(x)
fail.close()
    
    
print (bussid)

for buss in bussid:
#     sobib = True
    for buss2 in bussid:
        if (buss2[1]) < (buss[1]) and ((buss2[0]) > (buss[0]) or (buss2[0]) < (buss[0])) and  float(buss2[2]) <= float(buss[2]):
            if buss2 not in valik:
                valik.append(buss2)

valik.sort()
print(valik)