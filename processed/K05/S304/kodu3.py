ska = int(input("Sisesta suurte karpide hulk: "))
vka = int(input("Sisesta väikeste karpide hulk: "))
kmkk = int(input("Sisesta keedetud moosi mass: "))

def KarpideJ():
    if kmkk >= 5:
        sKA = kmkk/5
        vKA = kmkk - sKA
    elif  1 <= kmkk <= 4:
        vKA = kmkk
    
    
def moos(ska, vka, kmkk):
    KarpideJ()
    
    if ska < sKA:
        print(-1)

    elif vka < vKA:
        print(-1)
    
    elif sKA >= ska and vKA >= vka:
        print(summa)

    else:
        kmkk = 0
        print(-1)
        
sKA = int(kmkk/5)
jääk = int(kmkk - sKA*5)
vKA = jääk
summa = vKA+sKA
moos(ska, vka, kmkk)
            
            
      
    
    
    