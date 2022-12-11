from pykkar import *

create_world("""
###############
#            <#
#             #
#             #
#             #
#             #
#             #
#             #
#             #
#             #
#             #
###############
""")


tuled = 0
while tuled <= 5:
    if not is_wall():
        step()
    elif is_wall:
        right()
        tuled += 1
        if 1 < tuled < 6:
            paint()