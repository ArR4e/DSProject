from math import ceil

kogupikkus = int(input("Sisestage liini kogupikkus täisarvuna: "))
maxpikkus = int(input("Sisestage maksimaalne mastidevaheline kaugus täisarvuna: "))

mastidekogus = ceil(kogupikkus/maxpikkus) + 1
print(f"Vaja on vähemalt {mastidekogus} masti")