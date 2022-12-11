from pykkar import *
create_world("""
########
#      #
#   >  #
#      #
#      #
#      #
########
""")

värvitud_nurgad = 0
while not is_wall():
        step()
right()
while värvitud_nurgad < 4:
    while not is_wall():
        step()
    right()
    paint()
    värvitud_nurgad += 1