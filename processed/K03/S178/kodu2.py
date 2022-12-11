
from pykkar import *

create_world("""
########
#    < #
#      #
#      #
#      #
#      #
########
""")

samme_jäänud = 4
while samme_jäänud > 0:
    if is_wall():
        right()
        paint()
    else:
        step()
