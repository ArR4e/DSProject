from pykkar import *

create_world("""
########
#      #
#      #
#      #
#      #
#  >   #
########
""")
while is_wall() == False:
    step()
while is_wall() == True:
    right()

count = 0
while count != 4:
    count += 1
    while is_wall() == False:
        step()
    while is_wall() == True:
        right()
    paint()