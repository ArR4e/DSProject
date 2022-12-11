from pykkar import *
create_world("""
########
#     >#
#      #
#      #
#      #
#      #
########
""")

värvitud=0
sein1=0
while värvitud<4:  
   
    while is_wall():
        right()
        sein1+=1
    while not is_wall():
        step()
    if sein1==0 and is_wall():
            right()
            sein1+=1
    if sein1==1 and is_wall():
        right()
        paint()
        värvitud +=1
    
        
    
