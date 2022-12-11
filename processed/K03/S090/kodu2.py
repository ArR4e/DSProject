from pykkar import *
create_world("""
#############
#         < #
#           #
#           #
#           #
#           #
#############
""")
i=0
while i < 3:
    if get_direction() == "W":
        while not is_wall():
            step()
        if is_wall() == True:
            right()
            while not is_wall():
                step()
        if is_wall() == True:
            paint()
            right()
        while not is_wall():
            step()
        if is_wall() == True:
            right()
            paint() 
            while not is_wall():
                step()
        if is_wall() == True:
            paint()
            right()
        while not is_wall():
            step()
        if is_wall() == True:
            right()
            paint()
                     
    else:
        right()
    i+=1
    
     
exitonclick()