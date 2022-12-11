from pykkar import *
a = 0
create_world("""
########
#  ^   #
#      #
#      #
#      #
#      #
########
""")



while a < 4:
    while not is_wall():
        step()
    right()
    while not is_wall():
        step()
    paint()
    a += 1