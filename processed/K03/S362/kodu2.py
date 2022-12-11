from pykkar import *

# create_world võtab argumendiks mitmerealise sõne, mis esitab roboti maailma.
# Trellid tähistavad seinu, nooleke tähistab robotit.
# Noole suund (>, <, v või ^) tähistab roboti suunda.
create_world("""
########
#      #
#      #
#  <   #
#      #
#      #
########
""")

#samme_jäänud=4
#while samme_jäänud<4:
#    if is wall():
        #break
#    else:
#        step()
#        samme_jäänud=samme_jäänud-1
#right()
#right()
'''while not is_wall(): # is_wall() annab True, kui Pykkar on ninaga vastu seina
    step()
    
    if is_wall():
        right()
        paint()
        
        if is_painted():
            break
            right()'''
        
i=4

while not is_wall():
    step()
    if is_wall():
        break
    
while i>0:
    right()
    while not is_wall():
        step()
        if is_wall():
        
            paint()
            break
            
        
    i=i-1
right()






#while not is_wall():
    #step()
    #if is_wall():
        #paint()
        #right()
    
                
                
                #while not is_painted():
                    #step()
                    #if is_wall():
                        #break
                        #right()

# pööra ringi
#right()
#right()