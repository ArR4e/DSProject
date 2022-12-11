from pykkar import *
create_world("""
########
#      #
#      #
#      #
#   <  #
#      #
########
""")
a = 0

while not is_wall():
    step()
    if is_wall():
        right()
        break

while not is_painted():
    if not is_wall():
        step()
    elif is_wall():
        right()
        right()
        right()
        right()
        if not is_wall():
            step()
        elif is_wall():
            paint()
            a += 1
            if a == 4:
                break
            try:
                right()
                step()
            except:
                right()
                right() 
                step()
        
    