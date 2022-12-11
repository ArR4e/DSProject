import math
elektriliinipikkus=input("palun sisestage elektriliini pikkus(meetrites): ")
maxkaugus=input("palun sisestage elektripostide vahelise maksimaalkauguse(meetrites): ")
miinimumpostidearv = math.ceil(int(elektriliinipikkus) / int(maxkaugus))+1
print("Selle elektriliini ehitamiseks on vaja vähemalt ",miinimumpostidearv," elektriposti")