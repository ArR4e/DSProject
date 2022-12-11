from math import *

pikkus_txt=input("Elektriliini pikkus meetrites: ")
kaugus_txt=input("Elektripostide max kaugus meetrites: ")
pikkus_nr=int(pikkus_txt)
kaugus_nr=int(kaugus_txt)

postid=ceil(pikkus_nr/kaugus_nr)+1
print("Vajaminevate postide minimaalne arv: " , end=" ")
print(postid)