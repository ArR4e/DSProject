from math import ceil

pikkus = input("Sisestage liini pikkus: ")
max_vahe = input("Sisestage maksimaalne vahe: ")

print(ceil(int(pikkus) / int(max_vahe)) + 1)