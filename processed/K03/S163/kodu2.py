from pykkar import *

create_world("""
########
#      #
#      #
#      #
#     >#
#      #
########
""")

while True:
    if is_wall() == False:
        step()
    if is_wall() == True: #kui ees on sein, siis pöörame vasakule
        right()
        right()
        right()
        if is_wall() == True: #kui vasakul on sein, siis värvime ja pöörame tagasi ennast paremale
            paint()
            right()
            right()
        else:        #kui vasakul ei olnud seina, siis pöörame paremale
            right()
            right()
            

            
        
    
    



    