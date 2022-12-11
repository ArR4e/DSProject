from statistics import harmonic_mean
import matplotlib.pyplot as plt
def silu_andmed(list,n):
    i=1
    o=[]
    while not i > len(list):
        sisend_lõpp=i
        if i >= n:
            sisend_algus=i-n
        else:
            sisend_algus=0
        o+=[float(harmonic_mean(list[sisend_algus:sisend_lõpp]))]
        i+=1
    return o
e=open("aktsiad.txt","r") 
#e=input("algandmete fail", "r")
List=[]
for rida in e:
    #c+=rida.split(" ")
    List.append(float(rida.split(" ")[-1]))
e.close()
n=3
graafik = plt.figure()
ax = graafik.add_subplot(1,1,1)
ax.plot(List)
ax.plot(silu_andmed(List,n))
ax.set_xlabel("päevane aktsiahind")
ax.set_xlabel("aktsiahind peale hinna keskmistamist")
plt.show()
