liinipikkus=int(input("sisesta liini pikkus:"))
postidekaugus=int(input(" sisesta postide kaugus:"))
postidearv=(liinipikkus/postidekaugus+1)
import math
print(math.ceil(postidearv),"posti")