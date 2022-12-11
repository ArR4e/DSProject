start = open("luhendid.txt", "r")

#count = 0
uus_fail = ""
for line in start:
    paljas = line.strip()
    uus_rida = paljas.replace("mt", "mis teed")
    uus_fail += uus_rida
    
    
start.close()

finis = open("sonad.txt", "w")
finis.write(uus_fail)
finis.close()

#print(count)