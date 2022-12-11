from pykkar import *
create_world("""
######
# >  #
#    #
#    #
#    #
######
""")

for samm in range(4):
    while not is_wall():
        step()
    paint()
    right()