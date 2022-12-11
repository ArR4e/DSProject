from pykkar import *

create_world("""
########
#      #
#      #
#  <   #
#      #
#      #
########
""")

sein = 0 # параметр, сколько раз он коснулся стены
while True: #постоянный цикл    
    if is_wall():
        right()
        sein += 1
        if sein > 1:
            paint()
    else:
        step()
        
    


