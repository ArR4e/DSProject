
def loe_bussid(fail):
    with open(fail) as f:
        bussid = []
        for rida in f:
            buss = rida.strip().split()
            for i in range(2):
                buss[i]=(buss[i].replace(":", ""))
            buss = [int(x) for x in buss]
            bussid.append(buss)
    bussid.sort(key=lambda x: x[0])
    return bussid

def eemalda(a):
    halvad=[]
    for i in range(len(a)):
        for j in range(len(a)):
            if (a[i][0] < a[j][0] and a[i][1]>a[j][1] and a[i][2]>a[j][2]):
                halvad.append(a[i])
                break
    for el in halvad:
        a.remove(el)
        
def kellaajad(kell):
    kell = str(kell)
    return f"{kell[:-2]}:{kell[-2:]}"

fail = input("Sisesta failinimi: ")
bussid=loe_bussid(fail)
eemalda(bussid)

print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse: ")
for buss in bussid:
    print(f"{kellaajad(buss[0])} {kellaajad(buss[1])} {buss[2]}")
