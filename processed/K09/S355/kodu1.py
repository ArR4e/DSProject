from statistics import harmonic_mean
def silu_andmed(aktsiahinnad, n):
    aktsiahinnad = [float(i) for i in aktsiahinnad]
    m=1
    
    if m == 1 and n>0 and not m > n:
        print("Ma ei oska sedaa!!!")

    
    
    

aktsiafail = open("aktsiad.txt")
aktsiahinnad = ""
n = int(input("Mitme elemendi kaupa rakendatakse keskmistamist? "))
while True:
    loeaktsia = aktsiafail.readline().strip().split(",")
    aktsiahinnad += loeaktsia[-1]
    if loeaktsia == [""]:
        break
    
aktsiahinnad = aktsiahinnad.split(" ")
aktsiahinnad.remove(aktsiahinnad[0])

print(aktsiahinnad)
harmonic_mean(aktsiahinnad)
silu_andmed(aktsiahinnad, n)