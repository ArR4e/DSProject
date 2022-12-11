from statistics import harmonic_mean

# Teine osa: esialgse järjendi konverteerimine harmooniliselt keskmistatud elementidega järjendiks  
def silu_andmed(järjend1,n):
    if len(järjend1)<n:
        print("Väärtus n ei tohi olla suurem kui järjendi pikkus ja tühja järjendit tuleks vältida.")
        if järjend1==[]:
            järjend2=[]
        else:
            i=1
            järjend2=[]
            m=0
            murdarv=0
            murdarv=murdarv+1/järjend1[m]
            while i<=len(järjend1):
                
                Harm_keskm_element=i/murdarv
                
                
                järjend2=järjend2+[Harm_keskm_element]
                
                m=m+1
                if m>len(järjend1)-1:
                    break
                murdarv=murdarv+1/järjend1[m]
                i=i+1
                
            
        #print(järjend2)
    else:
    
        i=1
        järjend2=[]
        m=0
        murdarv=1/järjend1[m]
        while i<n:
            Harm_keskm_element=i/murdarv
            järjend2=järjend2+[Harm_keskm_element]
            i=i+1
            m=m+1
            murdarv=murdarv+1/järjend1[m]
    #5print(len(järjend2)) 
        j=0
        while i<=len(järjend1):
            a=järjend1[j:n]
            Harm_keskm_element=harmonic_mean(a)
            järjend2=järjend2+[Harm_keskm_element]
            j=j+1
            n=n+1
            i=i+1
        
    return järjend2
  
    
    
 # Esimene osa: esialgse järjendi loomine  faili nimi on: aktsiad.txt  
alg_andmed=input("Sisestage palun algandmetefaili nimi: ")
#alg_andmed="aktsiad.txt"
n=50
f=open(alg_andmed, "r", encoding="UTF-8")
järjend=[]
for rida in f:
    vahe_jarjend=rida.strip().split(",")
    järjend=järjend+[vahe_jarjend[1]]
#print(järjend)
f.close()
#sõne järjendi muutmine arvujärjendiks#
järjend1=list(map(float,järjend))
#järjend1=[7.34, 4.82, 5.33]

#print(järjend1)

järjend2=silu_andmed(järjend1,n)
#print(järjend2)
    
# print(len(järjend1))
# print(len(järjend2))

# Kolmas osa: graafikute joonisatmine kasutades matplotlib moodulit
import matplotlib.pyplot as plt

y1=järjend1
y2=järjend2
x1=x2=list(range(len(järjend1)))

print(y1)
print(y2)
# print(len(y1))
# print(len(y2))
# print(len(x1))

fig=plt.figure()
ax=fig.add_subplot(1,1,1)

ax.plot(x1,y1)
ax.plot(x2,y2)

ax.set_xlabel("x-telg")
ax.set_ylabel("y-telg")

plt.show()



    
    
    