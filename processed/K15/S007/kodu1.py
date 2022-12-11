import re

fail = open("aadressid.txt")

for rida in fail:
    
    if (re.search("ut[.]ee/~(\w+)/",rida)) != None:
        print((re.search("ut.ee/~(\w+)/",rida)).group(1))
    
    