from pykkar import *

create_world("""
#########
#  >    #
#       #
#       #
#       #
#       #
#########
""")
nurkade_arv = 0
while nurkade_arv < 4:
    while not is_wall():
        step()

    paint()
    right()
    nurkade_arv += 1