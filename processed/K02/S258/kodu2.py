from math import ceil
dist = int(input ("Sisesta liini pikkus (meetrites): "))
dist_max = int(input ("Sisesta postide max kaugus (meetrites): "))
print(ceil(dist/dist_max)+1)



