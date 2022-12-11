from pykkar import*
a=0

create_world("""
#########
#       #
#       #
#    >  #
#       #
#       #
#########
""")

while not is_wall():
    step()
    
right()

while a<4:
    while not is_wall():
        step()
    paint()
    right()
    a+=1
