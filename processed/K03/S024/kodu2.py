from pykkar import *

create_world("""
########
# <    #
#      #
#      #
#      #
#      #
########
""")

while not is_wall():
    step()
    if is_wall():
        right()
        break
        
if is_wall():
        right()
        
while not is_wall():
    step()
    if is_wall() and not is_painted():
        right()
        paint()
        step()
    

        
        
    
  
        
    

            
        


    
        
    
        




   