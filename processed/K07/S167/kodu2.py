#taksohinnad

o = open("taksohinnad.txt", "r")
u = open("taksohinnad.txt", "r")
kilomeeter = input("KM?")
#f = o.readline().strip()
#list = []
#for i in f:
#   list.append(i)

#list.index(",")


def tervik():
    f = o.readline().strip()
    list = []
    for i in f:
        list.append(i)

    uuslist = list[int(list.index(",")) + 1: int(len(list))]
    return uuslist

#rida1 = tervik().copy()
def uuslist():
    rida1 = tervik().copy()
    i1 = 0
    list1 = []
    while i1 < int(rida1.index(",")):
        d1 = rida1[i1]
        list1.append(d1)
        i1 += 1
    str1 = ""
    for i in list1:
        str1 += i

    i2 = rida1.index(",") + 1
    list2 = []
    while i2 < len(rida1):
        d2 = rida1[i2]
        list2.append(d2)
        i2 += 1
    str2 = ""
    for i in list2:
        str2 += i
    
    ennik = (float(str1), float(str2))
    
    return ennik

i = 0
summa = 0
list = []
while i < 3:
    rida1 = uuslist()
    hind = rida1[0] + rida1[1]*float(kilomeeter)
    list.append(hind)
    i += 1
    
parim = min(list)
indeks = list.index(float(parim))
#print(parim, indeks)
o.close()

def nimi():
    str = ""
    f1 = u.readline().strip()
    for i1 in f1:
        if i1 == ",":
            break
        str += i1
    return str

def nimed():
    list = []
    i = 0
    while i < 3:
        list.append(nimi())
        i += 1
    return list
print("Kõige odavam takso on", nimed()[indeks])
