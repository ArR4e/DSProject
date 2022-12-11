from math import ceil

distants = int(input("Sisestage elektriliini kogupikkus meetrites: "))
max_kaugus = int(input("Sisestage maksimaalne postidevaheline kaugus meetrites: "))

postide_arv = ceil(distants/max_kaugus) + 1

print(str(distants) + "m pikkuseks liini rajamiseks läheb vaja " + str(postide_arv) + " posti.")