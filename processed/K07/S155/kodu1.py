def poisse_ja_tüdrukuid(jrj):
    poisse = 0
    tüdrukuid = 0
    for element in jrj:
        if element.endswith(' P'):
            poisse += 1
            
        if element.endswith(' T'):
            tüdrukuid += 1
            
    return poisse, tüdrukuid
    
        
jrj = ['Jaan ', 'Nimetu ', 'Imelik ']


print(poisse_ja_tüdrukuid(jrj))       
        