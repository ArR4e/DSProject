def moos(s_karpe,v_karpe,moosi):
    karpe=0
    for i in range(s_karpe):
        if 5>moosi:
            break
        moosi-=5
        karpe+=1
    for j in range(v_karpe):
        if moosi==0:
            break
        moosi-=1
        karpe+=1
    if moosi!=0:
        karpe=-1
    return karpe
