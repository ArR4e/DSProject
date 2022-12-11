from pykkar import *

create_world("""
##########
#   >    #
#        #
#        #
##########
""")

kordus = -1
while kordus < 0:
    while not wall():
        step()
    right()
    kordus = 0
while kordus < 4:
    while not wall():
        step()
    paint()
    right()
    kordus = kordus +1