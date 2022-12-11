from pykkar import *
create_world("""
######
#  < #
#    #
######
""")
while not is_wall ():
    step()
while is_wall ():
    left()
    paint()