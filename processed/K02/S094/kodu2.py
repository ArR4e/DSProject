import math

user_pikkus = int(input("Liini pikkus meetrites: "))
user_max_dist = int(input("Postide maksimaalkaugus meetrites: "))

if(user_pikkus < user_max_dist):
    print("Liini pikkus on väiksem postide kaugusest.")

else:    
    tulemus = user_pikkus / user_max_dist
    tulemus = math.ceil(tulemus)
    print("Liini ehitamiseks on vaja minimaalselt " + str(tulemus) + " posti.")