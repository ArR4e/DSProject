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
for i in range(5):
    while not is_wall(): step()
    right()
    if i > 0: paint()