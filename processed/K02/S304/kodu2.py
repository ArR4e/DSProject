liiniPikkus = int(input("sisesta liini pikkus: "))
postideKaugus = int(input("sisesta postide kaugus: "))


from math import*

posteVaja = ceil((liiniPikkus/ postideKaugus) + 1)

print(int(posteVaja))