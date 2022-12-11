def moos(s,v,m):
    if s*5+v*1>=m:
        suuri=m
        i=0
        if m==0:
            return 0
        while i<s:
            suuri=suuri-5
            i+=1
            if suuri<5:
                break
        
        väikeseid=m-5*i
        if väikeseid<=v:
            kotte=i+väikeseid
            return kotte
           
        else:
            return -1
    else:
        return -1
s=int(input("Kui palju on suuri karpe?"))
v=int(input("Kui palju on väikseid karpe?"))
m=int(input("Kui palju on moosi kilogrammides?"))

moos(s,v,m)