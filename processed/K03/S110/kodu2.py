from pykkar import *

create_world("""
########
#      #
#      #
#  <   #
#      #
#      #
########
""")
i = 0

while not is_wall():
    step()
        
    
if is_wall() == True:
    right()
            
while i < 4:
    
    while is_wall() == False:
        step()
            
        if is_wall() == True:
            right()
            paint()
            i += 1
