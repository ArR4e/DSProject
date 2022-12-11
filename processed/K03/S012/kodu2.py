#kodu2 - pykkar
from pykkar import*

create_world("""
########
# >    #
#      #
#      #
#      #
#      #
########
""")
while get_direction() != "S":
    right()
while not is_wall():
    step()
while get_direction() != "E":
    right()
while not is_wall():
    step()
if is_wall():
    paint()
while is_wall():
    right()                     
while not is_wall():
    step()                        
if is_wall():
    paint()
while is_wall():
    right()
while not is_wall():
    step()                        
if is_wall():
    paint()
while is_wall():
    right()
while not is_wall():
    step()                        
if is_wall():
    paint()
while is_wall():
    right()
    
                        
                            
                            
