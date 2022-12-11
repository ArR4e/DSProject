from math import ceil
P = int(input("Sisesta liini pikkus (täisarvuna meetrites): "))
K = int(input("Sisesta postide maksimaalne kaugus teineteisest (täisarvuna meetrites): "))
print("Liini ehitamiseks on vaja vähemalt ", ceil(P/K+1), " posti.")