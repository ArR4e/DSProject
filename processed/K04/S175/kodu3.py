from turtle import*
from math import*

külgede_arv = 5
külje_pikkus = 50
pööre = 360 / külgede_arv
def kujund(arv, pikkus):
   a = 0
   b = 30
   c = 0
   while c < b:
       while  a < külgede_arv:
           forward(külje_pikkus)
           right(pööre)
           a += 1
       
   
   
kujund(külgede_arv, külje_pikkus)

        
    
    
