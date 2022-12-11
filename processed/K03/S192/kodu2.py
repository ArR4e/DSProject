from pykkar import *

create_world("""
########
#      #
#      #
#      #
# >    #
########
""")
nurk = 1
while nurk <= 4:
    while not is_wall():
        step()
    right()
    right()
    right() # Kontrollimaks, kas robotist vasakule jääb sein
    if is_wall() == False: # Lisakontroll, et tegemist oleks nurgaga, mitte küljega
        right()
        right()
    elif is_wall() == True:
        right()
        right()
        paint()
        nurk += 1 # Et robot teaks mitu nurka on veel vaja teha.
print("Nurgad on värvitud")        
