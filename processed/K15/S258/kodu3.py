fail=input("Sisesta failinimi: ")
fail="sõiduplaan.txt"
f=open(fail)
m=f.readlines()
f.close()
for x in range(len(m)):
    m[x]= m[x].strip().split(" ")
    m[x]= (m[x][0],m[x][1],m[x][2])

def grass(m,el=0):
    m2=m.copy()
    if el==len(m2):
        return m2
    for x in range(len(m2)):
        if m2[el][0]<m2[x][0] and m2[el][1]>m2[x][1] and int(m2[el][2])>int(m2[x][2]):
            m2.remove(m2[el])
            return grass(m2,el)
    return grass(m2,el+1)

m=grass(m)
m.sort()
print("Esimesest linnast teise sõitmiseks võiksid kaaluda järgmisi busse:")
for x in m:
    print(x[0],x[1],x[2])