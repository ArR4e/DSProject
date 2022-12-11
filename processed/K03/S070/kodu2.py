from pykkar import *

create_world("""
########
#      #
#      #
#  <   #
#      #
#      #
########""")
while is_wall() is False:
        step()
right()
for i in range (0, 4):
    while is_wall() is False:
         step()
    right()
    paint()
 
    
