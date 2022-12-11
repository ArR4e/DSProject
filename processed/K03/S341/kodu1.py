aastatulu = float(input("Sisestage aastatulu : "))
if aastatulu <= 6000:
    maksutulu = aastatulu
    print("Maksuvaba tulu on " + str(round(aastatulu, 2)) + " eurot.") 
    
elif 6000 <= aastatulu <= 14400:
    maksutulu = 6000
    print("Maksuvaba tulu on " + str(round(maksutulu, 2)) + " eurot.") 
    
elif 14440 <= aastatulu <= 25200:
    maksutulu = (6000- 6000/10800*(aastatulu-14400))
    print("Maksuvaba tulu on " + str(round(maksutulu, 2)) + " eurot.")
    
elif aastatulu > 25200:
    maksutulu = 0
    print("Maksuvaba tulu on " + str(round(maksutulu, 2)) + " eurot.") 
    

   
