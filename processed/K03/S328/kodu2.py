from pykkar import *

create_world("""
########
#      #
#      #
#      #
#      #
#  <   #
########
""")


while is_wall() is False or is_wall() is True and is_painted() is False:
    if is_wall() is False:
        step()
    elif is_wall() is True:
        paint()
        right()
        continue

    