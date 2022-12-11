from math import *
a=float(input("Sisestage liini kogupikkus:"))
b=float(input("Sisestage maksimaalne kahe posti vahemaa:"))
print("Poste on vaja vähemalt:"+str(floor(a/b)+1))