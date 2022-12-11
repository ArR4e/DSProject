f = open("sõiduplaan.txt", encoding="UTF-8")
max_ = 0
max_mins = 0
kestus = []
hind = []

for i in f:
    ajutine = list(i.split(" "))
    kestus.append((str(abs(int(ajutine[0].split(":")[0]) - int(ajutine[1].split(":")[0])))) + ":" + str(abs(int(ajutine[0].split(":")[1]) - int(ajutine[1].split(":")[1]))))
    hind.append(int(ajutine[2].strip()))
    f.close()
    
for i in kestus:
    if (int(i.split(":")[0]) * 60 + int(i.split(":")[1])) > max_mins:
        max_ = i
        max_mins = int(i.split(":")[0]) * 60 + int(i.split(":")[1])

for i in f:
    