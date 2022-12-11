from pykkar import *

create_world("""
########
#      #
#      #
#   >  #
#      #
#      #
########
""")
while is_wall() == False:
    step()
while is_wall() == True:
    right()
for i in range(4):
    while is_wall() == False:
        step()
    while is_wall() == True:
        paint()
        right()


