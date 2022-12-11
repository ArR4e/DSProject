fail1 = open("lapsed.txt", "r", encoding = "utf-8")
fail2 = open("nimed.txt", "r", encoding = "utf-8")
nimed = {}

for rida in fail1:
    rida = rida.strip().split(" ")
    laps = rida[0]
    vanem = rida[1]
    print(laps)
    
for rida in fail2:
    rida = rida.strip().split(" ")
    isikukood = rida[0]
    isik = rida[1] + " " + rida[2]
    print(isik)
    
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")
