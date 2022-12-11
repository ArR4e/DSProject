from copy import deepcopy
with open(input("Sisesta failinimi: "),"r") as f:
    x = f.readlines()
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
y = deepcopy(x)
for l in x:
    n = l.strip().split(" ")
    for k in x:
        m = k.strip().split(" ")
        if n == m:
            pass
        else:
            if n[0]<m[0] and n[1]>m[1]:
                if int(n[2])>int(m[2]):
                    try:
                        y.remove(l)
                    except:
                        pass
z = sorted(y,key=lambda x: x.split(" ")[0])
[print(i.strip()) for i in z]