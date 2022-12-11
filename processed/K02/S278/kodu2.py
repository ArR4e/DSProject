from __future__ import division
pikkus = int(input("Tere! Palun sisesta liini pikust ja vajuta ENTER:"))
postide_vaheline_pikkus = int(input("Tere! Palun sisesta postide vaheline pikkus ja vajuta ENTER:"))
import math
postid = (math.ceil(float(pikkus) / float(postide_vaheline_pikkus))) + 1
if postid <= 0 :
    print("Proovige veel kord palun")
else:
        if postid == 1:
            print("Teil on",postid,"post")
        elif  postid > 1:
            print("Teil on",postid,"posti")
            

