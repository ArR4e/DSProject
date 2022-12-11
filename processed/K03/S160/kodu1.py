import math

aastatulu = float(input("Sisestage oma aastatulu:"))
maksuvaba = round(aastatulu, 2)
if aastatulu < 6000.00 or aastatulu == 6000.00 :
    print("Teie aastatulu on " + str(maksuvaba) + " eurot")
    
elif 14400.00 >= aastatulu > 6000.00 :
    maksuvaba = round(aastatulu, 2)
    print ("Teie maksuvaba tulu on 6000 eurot aastas")
    
elif 25200 >= aastatulu > 14400.00 :
    maksuvaba1 = round(6000-6000/10800*(aastatulu-14400), 2)
    print ("Teie maksuvaba tulu on " + str(maksuvaba1) + " eurot")

elif aastatulu > 25200.00 :
    print("Teie maksuvaba tulu on 0 eurot")