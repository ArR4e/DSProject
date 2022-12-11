from pykkar import *
create_world("""
########
#      #
#  >   #
#      #
#      #
#      #
########
""")
while not is_wall():
    step()
    if is_wall():
        right()
        pass
    
        i=0
        while not is_wall():
            step()
            while is_wall() and i<4:
                paint()
                if is_painted():
                    right()
                    i+=1
        
