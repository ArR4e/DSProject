# < >
def moos(S, V, KG):
    S_arv=0
    V_arv=0
    for i in range(S):
        if KG==0:
            return(0)
            
        if KG<5:
            break
        else:
            KG=KG-5
            S_arv+=1
            S-=1
            if S==0:
                break
            
    while True:
        if KG==0:
            return(S_arv)
            
        if KG>0 and KG<=V:
            V_arv+=1
            if V_arv==KG:
                return(V_arv + S_arv)
                
        else:
            return(-1)
            
    
moos(3,3,8)    
            