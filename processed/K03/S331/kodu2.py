from pykkar import *
create_world("""
########
#      #
#  >   #
#      #
#      #      
########
""")
while True:
    while not is_wall(): 
        step()
    right()
    right()
    right()
    if is_wall():
        paint()
        right()
        right()
        while not is_wall(): 
            step()
    else:
        right()
        right()
        if is_wall():
            paint()
            right()
            right()
            while not is_wall():
                step()
        else:
            while not is_wall():
                step()
exitonclick()