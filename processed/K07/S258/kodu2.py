f = open("taksohinnad.txt")




def hind(jär,km):
    nimed.append(jär[0])
    hinnad.append(float(jär[1])+float(jär[2])*km)
    
    



km = float(input("Sisesta tee pikkus kilomeetrites: "))

nimed=[]
hinnad=[]



for line in f:
    hind(line.strip().split(","),km)
try:
    print("Kõige odavam on "+str(nimed[hinnad.index(min(hinnad))])+".")
except:
    pass


f.close()