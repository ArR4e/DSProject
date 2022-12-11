#VÄGA-VÄGA ALGELINE VARIANT!

failinimi = input("Sisesta failinimi: ")
def loe_failist(failinimi):  
    f = open(failinimi, encoding="UTF-8")
    järjend=[]
    uus=[]
    for rida in f:
        rida = rida.strip().split(" ")
        väljumine = rida[0]
        saabumine = rida[1]
        hind = rida[2]
        järjend.append(väljumine)
        järjend.append(saabumine)
        järjend.append(hind)       
    return järjend

sõiduplaani_järjend= loe_failist(failinimi)
print(sõiduplaani_järjend)

def töötle(sõiduplaani_järjend):
    for i in range(len(sõiduplaani_järjend)):
        if sõiduplaani_järjend[0]>sõiduplaani_järjend[3]:
            break
        else:
            if sõiduplaani_järjend[1]>sõiduplaani_järjend[4]:
                break
            else:
                return "sobilik"
        
    return

print(töötle(sõiduplaani_järjend))
    

