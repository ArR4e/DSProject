from pykkar import*
create_world("""
########
#  >   #
#      #
#      #
#      #
#      #
########
""")

while not is_wall():
    step()
right()
i=0
while i<4:
    while not is_wall():
        step()
    right()
    paint()
    i+=1