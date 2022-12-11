import math

#defineerime koogi hinna arvutamise meetodi
def koogi_hind(name, size):

    if(name.lower() == "šokolaadikook"):
        return round(math.pi * size * size * 0.06, 2)

    elif(name.lower() == "ploomikook"):
        return round(math.pi * size * size * 0.04, 2)

    elif(name.lower() == "napoleoni kook"):
        return round(size * size * 0.10, 2)

    else:
        #kui koogi hinda ei ole "andmebaasis", viskame exceptioni
        raise Exception("Sellist kooki andmebaasist ei leitud")

#muutujad
cakename = ""
cakesize = 0

#Alustame programmitsükliga
try:
    while(True):

        cakename = str(input("Sisestage koogi nimi: "))

        #katkestame tsükli kui koogi nime ei sisestatud
        if(cakename == ""):
            break
        
        #saime nime, seega küsime mõõtu
        cakesize = float(input("Sisestage koogi mõõt: "))

        #väljastame koogi hinna
        print(koogi_hind(cakename, cakesize))

except Exception as e:
    #prindime meetodist visatud exceptioni
    print(e)