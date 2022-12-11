import matplotlib.pyplot as plt
lis=[]
def silu_andmed(järjend,n):
    if len(järjend)==0:
        return []
    vastus=[]
    murd=0
    arv=0
    for i in range(len(järjend)):
        murd=0
        if i<n:
            arv=i+1
            for l in range(i+1):
                murd=murd+1/järjend[l]
            arv=arv/murd
        elif i>=n:
            arv=n
            for l in range(n):
                murd=murd+1/järjend[i]
           # print(murd)
            arv=arv/(murd)
            #print(arv)
        vastus.append(arv)
    return vastus
koht=str(input("Sisestage faili nimi: "))
f=open(koht,"r")
numbrid=[]
for rida in f:
    a=f.readline()
    e=a.split(", ")
    if len(e)==2:
        e[1]=e[1].rstrip()
        e[1]=float(e[1])
        numbrid.append(e[1])
kuud         = [  1,    4,    5,    6,    7,    8,    9,   10,  11,  12]
sissetulekud = [710, 1200, 1445, 1690, 1350, 1223, 1470, 1200, 808, 698]
väljaminekud = [700, 1160, 1556, 1520, 1415, 1180, 1770,  500, 408, 505]

fig = plt.figure()           # Kõigepealt loome joonist tähistava objekti
ax = fig.add_subplot(1,1,1)  # ja lisame joonisele joonestusala.

ax.plot(kuud, sissetulekud, "o-", label="Sissetulekud")
ax.plot(kuud, väljaminekud, "^-r", label="Väljaminekud")

ax.set_xlabel("Kuud")
ax.set_ylim(0, 2000)         # Määrame y-telje nähtavuspiirkonna
ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12])  # ja x-telje märgid
ax.legend()

plt.show() 
silu_andmed(numbrid,50)

