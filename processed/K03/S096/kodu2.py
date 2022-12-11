# Pykkar igas maailma nurgas

from pykkar import *

create_world("""
#####
#   #
#   #
#   #
#   #
#v  #
#####
""")

#turn left
def left():
    rigth()
    right()
    right()

# move to the wall
def forward():
    while not is_wall():
        step()

#get N direction and go to the NE corner
def northeast():
    while get_direction() != "N":
        right()
    forward()
    right()
    forward()

northeast()
#paint world corners
while not is_painted():
    paint()
    right()
    forward()