fail= input("Sisesta failinimi: ")

järjend = []
with open(fail, "r") as f:
    for rida in f:
        ennik = ((rida.strip().split(" ", 3)))
        järjend.append(ennik)
        
for i in range(2):
    for buss in järjend:
        for buss2 in järjend:
            if buss != buss2:
                if buss[0] > buss2[0]:
                    if buss[1] < buss2[1]:
                        if int(buss[2]) < int(buss2[2]):
                            järjend.remove(buss2)
järjend.sort()
for el in järjend:
    sõne = el[0] + " " + el[1] + " " + el[2]
    print(sõne)