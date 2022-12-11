from math import *
pikkus = int(input("palun sisestage elektriliini pikkus: "))
vahe =  int(input("palun sisestage postide vaheline maksimaalne kaugus: "))
postid = pikkus / vahe
alguspost = 1
print("elektriliini ehitamiseks läheb vaja minimaalselt " + str(int(ceil(postid) + alguspost)) + " posti")
             