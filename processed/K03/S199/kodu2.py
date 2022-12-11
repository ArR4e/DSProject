from pykkar import *
create_world("""
########
#      #
#   <  #
#      #
#      #
#      #
########
""")
värvitud = 0
while värvitud == 0:  
    while not is_wall():
        step()
        if is_wall():
            right()
            step()
            if is_wall():
                paint()
                värvitud = värvitud + 1
                
while värvitud < 4 and värvitud > 0:
    right()
    while not is_wall():
        step()
        if is_wall():
            paint()
            värvitud = värvitud + 1
            right()
            if värvitud == 4:
                left()
           
         
           

       
            
        
    
